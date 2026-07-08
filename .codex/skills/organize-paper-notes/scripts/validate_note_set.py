#!/usr/bin/env python3
"""Validate an Obsidian paper note set without modifying files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]")
EMPTY_HEADING_RE = re.compile(r"^#{1,6}\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"TODO|FIXME|\[TODO|\{\{[^}]+\}\}|\.\.\.", re.IGNORECASE)


def find_vault_root(start: Path) -> Path:
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for candidate in [current, *current.parents]:
        if (candidate / "99_Templates").exists() and (candidate / "90_Sources").exists():
            return candidate
    return Path.cwd().resolve()


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix.lower() == ".md":
            files.append(path)
    return sorted(dict.fromkeys(files))


def link_exists(vault_root: Path, source: Path, target: str) -> bool:
    target = target.strip()
    if not target:
        return True

    candidates: list[Path] = []
    raw = Path(target)
    if raw.suffix:
        candidates.append(vault_root / raw)
        candidates.append(source.parent / raw)
    else:
        candidates.extend(
            [
                vault_root / raw,
                vault_root / f"{target}.md",
                source.parent / raw,
                source.parent / f"{target}.md",
            ]
        )
    if any(candidate.exists() for candidate in candidates):
        return True

    if "/" not in target and "\\" not in target:
        names = [target] if Path(target).suffix else [f"{target}.md"]
        return any(next(vault_root.rglob(name), None) is not None for name in names)

    return False


def registry_duplicate_ids(vault_root: Path) -> list[str]:
    registry = vault_root / "90_Sources" / "Resource Registry.md"
    if not registry.exists():
        return []

    ids: dict[str, int] = {}
    for line in registry.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\|\s*`([^`]+)`\s*\|", line)
        if match:
            ids[match.group(1)] = ids.get(match.group(1), 0) + 1
    return sorted(identifier for identifier, count in ids.items() if count > 1)


def pdf_residue_errors(paths: list[Path], files: list[Path], vault_root: Path) -> list[str]:
    pdfs: set[Path] = set()

    for path in paths:
        if path.is_dir():
            pdfs.update(path.rglob("*.pdf"))
        elif path.is_file():
            pdfs.update(path.parent.glob(f"{path.stem}.pdf"))

    for file in files:
        pdfs.update(file.parent.glob(f"{file.stem}.pdf"))

    errors = []
    for pdf in sorted(pdfs):
        try:
            shown = pdf.relative_to(vault_root)
        except ValueError:
            shown = pdf
        errors.append(f"{shown}: PDF remains in vault; ask the user whether to delete it after organization")
    return errors


def chinese_allowed(path: Path, line: str) -> bool:
    if path.name == "Vocabulary.md":
        return "| " in line or "CN gloss" in line
    return False


def validate(files: list[Path], input_paths: list[Path], vault_root: Path) -> list[str]:
    errors: list[str] = []

    for path in files:
        text = path.read_text(encoding="utf-8")

        if EMPTY_HEADING_RE.search(text):
            errors.append(f"{path}: empty Markdown heading")

        for match in PLACEHOLDER_RE.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path}:{line_no}: placeholder text: {match.group(0)}")

        if text.count("$$") % 2:
            errors.append(f"{path}: unmatched $$ LaTeX block delimiter")

        for line_no, line in enumerate(text.splitlines(), 1):
            if HAN_RE.search(line) and not chinese_allowed(path, line):
                errors.append(f"{path}:{line_no}: unexpected Chinese text")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1)
            if not link_exists(vault_root, path, target):
                line_no = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path}:{line_no}: unresolved wikilink [[{target}]]")

    for duplicate in registry_duplicate_ids(vault_root):
        errors.append(f"90_Sources/Resource Registry.md: duplicate registry ID `{duplicate}`")

    errors.extend(pdf_residue_errors(input_paths, files, vault_root))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a paper note set.")
    parser.add_argument("paths", nargs="+", help="Markdown files or directories to validate")
    parser.add_argument("--vault-root", default="", help="Vault root; auto-detected when omitted")
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.paths]
    missing = [str(path) for path in input_paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing path: {path}", file=sys.stderr)
        return 2

    vault_root = Path(args.vault_root).resolve() if args.vault_root else find_vault_root(input_paths[0])
    files = iter_markdown(input_paths)
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 2

    errors = validate(files, input_paths, vault_root)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed for {len(files)} Markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
