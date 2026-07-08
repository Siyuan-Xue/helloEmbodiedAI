#!/usr/bin/env python3
"""Update Embodied AI source snapshots and generate an Obsidian registry.

The script is intentionally conservative:
- It writes generated output to `Resource Registry.generated.md`.
- It never edits curated notes or area maps.
- It can run offline against existing README snapshots.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPOS_DIR = ROOT / "90_Sources" / "repos"
SNAPSHOT_DIR = ROOT / "90_Sources" / "snapshots"
GENERATED_REGISTRY = ROOT / "90_Sources" / "Resource Registry.generated.md"
GENERATED_LOG = ROOT / "90_Sources" / "Repository Update Log.generated.md"


SOURCES = [
    {
        "key": "hcplab",
        "repo": "HCPLab-SYSU/Embodied_AI_Paper_List",
        "url": "https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List",
        "branches": ["main", "master"],
        "role": "Backbone taxonomy for embodied AI papers.",
        "default_area": "platform",
    },
    {
        "key": "zchoi",
        "repo": "zchoi/Awesome-Embodied-Robotics-and-Agent",
        "url": "https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent",
        "branches": ["main", "master"],
        "role": "Frontier robotics and embodied agent tracker.",
        "default_area": "agent",
    },
    {
        "key": "milkclouds",
        "repo": "MilkClouds/awesome-vla-study",
        "url": "https://github.com/MilkClouds/awesome-vla-study",
        "branches": ["main", "master"],
        "role": "VLA study roadmap.",
        "default_area": "vla",
    },
    {
        "key": "changanvr",
        "repo": "ChanganVR/awesome-embodied-vision",
        "url": "https://github.com/ChanganVR/awesome-embodied-vision",
        "branches": ["main", "master"],
        "role": "Embodied vision and navigation resources.",
        "default_area": "navigation",
    },
    {
        "key": "awesome-touch",
        "repo": "linchangyi1/Awesome-Touch",
        "url": "https://github.com/linchangyi1/Awesome-Touch",
        "branches": ["main", "master"],
        "role": "Tactile sensing and contact-rich manipulation resources.",
        "default_area": "interaction",
    },
]


@dataclasses.dataclass
class Resource:
    identifier: str
    title: str
    type: str
    area: str
    task: str
    method: str
    modality: str
    embodiment: str
    source_repo: str
    section: str
    url: str
    status: str = "inbox"


def run_command(args: list[str], cwd: Path) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            args,
            cwd=str(cwd),
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    return result.returncode == 0, result.stdout.strip()


def repo_slug(source: dict[str, str]) -> str:
    return source["repo"].replace("/", "--")


def snapshot_path(source: dict[str, str]) -> Path:
    return SNAPSHOT_DIR / f"{repo_slug(source)}.README.md"


def local_readme_candidates(source: dict[str, str]) -> list[Path]:
    base = REPOS_DIR / repo_slug(source)
    return [base / "README.md", base / "readme.md", snapshot_path(source)]


def fetch_raw_readme(source: dict[str, str]) -> tuple[str | None, str]:
    last_error = ""
    owner_repo = source["repo"]
    for branch in source["branches"]:
        url = f"https://raw.githubusercontent.com/{owner_repo}/{branch}/README.md"
        try:
            with urllib.request.urlopen(url, timeout=45) as response:
                text = response.read().decode("utf-8", errors="replace")
            return text, f"downloaded {url}"
        except (urllib.error.URLError, TimeoutError, UnicodeError) as exc:
            last_error = f"{url}: {exc}"
    return None, last_error


def ensure_source_text(source: dict[str, str], allow_network: bool) -> tuple[str | None, str]:
    repo_dir = REPOS_DIR / repo_slug(source)
    if (repo_dir / ".git").exists() and allow_network:
        ok, output = run_command(["git", "pull", "--ff-only"], repo_dir)
        if not ok:
            return None, f"git pull failed: {output}"

    if not repo_dir.exists() and allow_network:
        ok, output = run_command(
            ["git", "clone", "--depth", "1", source["url"], str(repo_dir)],
            ROOT,
        )
        if not ok:
            # Continue to raw README fallback.
            pass

    for candidate in local_readme_candidates(source):
        if candidate.exists():
            return candidate.read_text(encoding="utf-8", errors="replace"), f"read {candidate.relative_to(ROOT)}"

    if allow_network:
        text, message = fetch_raw_readme(source)
        if text:
            SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
            snapshot_path(source).write_text(text, encoding="utf-8")
            return text, message
        return None, message

    return None, "no local README snapshot"


def strip_markdown(value: str) -> str:
    value = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[*_~>#]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -:\t")


def first_url(value: str) -> str:
    match = re.search(r"https?://[^\s)>\"]+", value)
    return match.group(0).rstrip(".,") if match else ""


def classify_type(text: str, section: str) -> str:
    hay = f"{text} {section}".lower()
    if any(word in hay for word in ["survey", "surveys", "review", "综述"]):
        return "survey"
    if any(word in hay for word in ["dataset", "data set", "benchmark data"]):
        return "dataset"
    if any(word in hay for word in ["simulator", "simulation", "environment", "env "]):
        return "simulator"
    if any(word in hay for word in ["benchmark", "leaderboard", "evaluation", "eval"]):
        return "benchmark"
    if any(word in hay for word in ["github", "code", "toolkit", "library", "software", "repo"]):
        return "code"
    if any(word in hay for word in ["course", "lecture", "tutorial", "study", "week "]):
        return "course"
    if any(word in hay for word in ["sensor", "hardware", "product", "commercial", "gel", "tactile"]):
        return "product"
    if any(word in hay for word in ["lab", "group", "institute"]):
        return "lab"
    if any(word in hay for word in ["arxiv", "paper", "cvpr", "icra", "iros", "neurips", "icml", "corl"]):
        return "paper"
    return "note"


def classify_area(text: str, section: str, default_area: str) -> str:
    hay = f"{text} {section}".lower()
    if any(word in hay for word in ["vla", "vision-language-action", "robot foundation", "rt-1", "rt-2", "openvla"]):
        return "vla"
    if any(word in hay for word in ["world model", "real2sim", "real-to-sim", "sim-to-real", "sim2real"]):
        return "world-model"
    if any(word in hay for word in ["navigation", "nav", "vln", "objectnav", "pointgoal", "imagegoal", "eqa"]):
        return "navigation"
    if any(word in hay for word in ["manipulation", "grasp", "rearrangement", "dexterous", "tactile", "touch", "hri"]):
        return "interaction"
    if any(word in hay for word in ["perception", "grounding", "slam", "mapping", "segmentation", "3d"]):
        return "perception"
    if any(word in hay for word in ["agent", "planning", "memory", "tool use", "multi-agent"]):
        return "agent"
    if any(word in hay for word in ["dataset", "simulator", "benchmark", "robot", "hardware", "sensor"]):
        return "platform"
    if any(word in hay for word in ["reinforcement", "diffusion", "flow matching", "imitation", "control"]):
        return "foundation"
    return default_area


def classify_task(text: str, section: str) -> str:
    hay = f"{text} {section}".lower()
    for value, words in [
        ("objectnav", ["objectnav", "object navigation"]),
        ("vln", ["vln", "vision-language navigation"]),
        ("manipulation", ["manipulation", "grasp", "pick", "place"]),
        ("rearrangement", ["rearrangement", "rearrange"]),
        ("tactile", ["tactile", "touch"]),
        ("grounding", ["grounding", "grounded"]),
        ("planning", ["planning", "planner", "plan"]),
    ]:
        if any(word in hay for word in words):
            return value
    return ""


def classify_method(text: str, section: str) -> str:
    hay = f"{text} {section}".lower()
    for value, words in [
        ("flow-matching", ["flow matching", "flow-matching"]),
        ("diffusion", ["diffusion"]),
        ("imitation-learning", ["imitation", "behavior cloning"]),
        ("world-model", ["world model"]),
        ("vla", ["vla", "vision-language-action"]),
        ("vlm", ["vlm", "vision-language"]),
        ("llm", ["llm", "large language"]),
        ("rl", ["reinforcement", " rl ", "ppo", "q-learning"]),
    ]:
        if any(word in hay for word in words):
            return value
    return ""


def classify_modality(text: str, section: str) -> str:
    hay = f"{text} {section}".lower()
    hits = []
    for value, words in [
        ("vision", ["vision", "visual", "image", "video", "rgb"]),
        ("language", ["language", "text", "instruction"]),
        ("action", ["action", "control", "policy"]),
        ("tactile", ["tactile", "touch", "force"]),
        ("audio", ["audio", "sound"]),
        ("proprioception", ["proprioception", "state", "joint"]),
    ]:
        if any(word in hay for word in words):
            hits.append(value)
    return "multimodal" if len(hits) > 1 else (hits[0] if hits else "")


def classify_embodiment(text: str, section: str) -> str:
    hay = f"{text} {section}".lower()
    for value, words in [
        ("humanoid", ["humanoid"]),
        ("dexterous-hand", ["dexterous", "hand"]),
        ("legged", ["legged", "quadruped"]),
        ("mobile-robot", ["mobile robot", "navigation", "nav"]),
        ("manipulator", ["manipulator", "arm", "gripper"]),
        ("virtual-agent", ["virtual", "simulator", "environment"]),
    ]:
        if any(word in hay for word in words):
            return value
    return ""


def make_identifier(source_key: str, title: str, section: str) -> str:
    raw = f"{source_key}:{section}:{title}".encode("utf-8", errors="ignore")
    digest = hashlib.sha1(raw).hexdigest()[:10]
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:40]
    return f"{source_key}-{slug}-{digest}" if slug else f"{source_key}-{digest}"


def parse_readme(source: dict[str, str], text: str) -> list[Resource]:
    resources: list[Resource] = []
    headings: list[str] = []

    for line in text.splitlines():
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            level = len(heading.group(1))
            title = strip_markdown(heading.group(2))
            headings = headings[: level - 1] + [title]
            continue

        item = re.match(r"^\s*(?:[-*+]|\d+[.)])\s+(.+?)\s*$", line)
        if not item:
            continue

        raw = item.group(1)
        if len(raw) < 8:
            continue

        section = " > ".join(headings)
        title = strip_markdown(raw)
        if not title or title.lower() in {"paper", "code", "project", "dataset"}:
            continue
        if len(title) > 140:
            title = title[:137] + "..."

        resource_type = classify_type(raw, section)
        area = classify_area(raw, section, source["default_area"])
        resources.append(
            Resource(
                identifier=make_identifier(source["key"], title, section),
                title=title.replace("|", "\\|"),
                type=resource_type,
                area=area,
                task=classify_task(raw, section),
                method=classify_method(raw, section),
                modality=classify_modality(raw, section),
                embodiment=classify_embodiment(raw, section),
                source_repo=source["key"],
                section=section.replace("|", "\\|"),
                url=first_url(raw),
            )
        )

    return resources


def fallback_resource(source: dict[str, str], message: str) -> Resource:
    return Resource(
        identifier=f"source-{source['key']}",
        title=f"{source['repo']} ({message})",
        type="note",
        area=source["default_area"],
        task="",
        method="",
        modality="",
        embodiment="",
        source_repo=source["key"],
        section="source repository",
        url=source["url"],
        status="sync-needed",
    )


def markdown_link(title: str, url: str) -> str:
    return f"[{title}]({url})" if url else title


def render_registry(resources: list[Resource], messages: list[str]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = [
        "---",
        'title: "Resource Registry.generated"',
        "type: generated-registry",
        "status: generated",
        "tags:",
        "  - generated",
        "  - registry",
        "  - embodied-ai",
        "---",
        "",
        "# Resource Registry.generated",
        "",
        f"Generated at: `{now}`",
        "",
        "Review these rows before promoting them into curated Obsidian notes or Zotero.",
        "",
        "## Source Status",
        "",
    ]
    rows.extend(f"- {message}" for message in messages)
    rows.extend(
        [
            "",
            "## Resources",
            "",
            "| ID | Title | Type | Area | Task | Method | Modality | Embodiment | Source | Section | Status |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for resource in resources:
        title = markdown_link(resource.title, resource.url)
        rows.append(
            f"| `{resource.identifier}` | {title} | {resource.type} | {resource.area} | "
            f"{resource.task} | {resource.method} | {resource.modality} | {resource.embodiment} | "
            f"{resource.source_repo} | {resource.section} | {resource.status} |"
        )
    rows.append("")
    return "\n".join(rows)


def render_log(messages: list[str], resource_count: int) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "---",
        'title: "Repository Update Log.generated"',
        "type: generated-update-log",
        "status: generated",
        "tags:",
        "  - generated",
        "  - update-log",
        "  - embodied-ai",
        "---",
        "",
        "# Repository Update Log.generated",
        "",
        f"Generated at: `{now}`",
        f"Generated resources: `{resource_count}`",
        "",
        "## Source Results",
        "",
    ]
    lines.extend(f"- {message}" for message in messages)
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-network", action="store_true", help="Use only local clones and README snapshots.")
    args = parser.parse_args(argv)

    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

    allow_network = not args.no_network
    all_resources: list[Resource] = []
    messages: list[str] = []

    for source in SOURCES:
        text, message = ensure_source_text(source, allow_network=allow_network)
        if text:
            parsed = parse_readme(source, text)
            all_resources.extend(parsed)
            messages.append(f"`{source['key']}`: {message}; parsed {len(parsed)} resources.")
        else:
            all_resources.append(fallback_resource(source, message))
            messages.append(f"`{source['key']}`: {message}; created sync-needed placeholder.")

    GENERATED_REGISTRY.write_text(render_registry(all_resources, messages), encoding="utf-8")
    GENERATED_LOG.write_text(render_log(messages, len(all_resources)), encoding="utf-8")
    print(f"Wrote {GENERATED_REGISTRY.relative_to(ROOT)}")
    print(f"Wrote {GENERATED_LOG.relative_to(ROOT)}")
    print(f"Resources: {len(all_resources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
