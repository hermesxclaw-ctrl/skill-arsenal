#!/usr/bin/env python3
"""
skill-arsenal validator — enforces the authoring contract on every SKILL.md.

Checks (mirrors hermes-agent's skill_manager_tool.py constraints):
  1. Frontmatter starts at byte 0 with '---'
  2. Closes with '\\n---\\n' before the body
  3. YAML parses as a mapping
  4. 'name' present, lowercase+hyphens, <= 64 chars
  5. 'description' present, <= 1024 chars, starts with 'Use when'
  6. Non-empty body after closing frontmatter
  7. Total file <= 100_000 chars
  8. Recommended: version/author/license/metadata.hermes.{tags,related_skills}
  9. Structure: has ## Common Pitfalls and ## Verification Checklist

Exit code 0 = all pass, 1 = any failure. Runs standalone (stdlib only).

Usage:
  python scripts/validate_skills.py              # check skills/ recursively
  python scripts/validate_skills.py --strict     # also flag missing recommended fields
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # fall back to a minimal frontmatter parse below

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

MAX_NAME_LEN = 64
MAX_DESC_LEN = 1024
MAX_CONTENT_LEN = 100_000


def parse_frontmatter(text: str):
    """Return (frontmatter_dict_or_None, error_str)."""
    if not text.startswith("---"):
        return None, "file does not start with '---' at byte 0"
    # split on the closing '---' after the opening one
    m = re.search(r"\n---\s*\n", text[3:])
    if not m:
        return None, "no closing '---' found for frontmatter"
    fm_text = text[3 : 3 + m.start()]
    body = text[3 + m.end() :]
    if not body.strip():
        return None, "empty body after frontmatter"
    if yaml is not None:
        try:
            data = yaml.safe_load(fm_text)
        except Exception as exc:  # noqa: BLE001
            return None, f"YAML parse error: {exc}"
    else:
        # minimal fallback: name:/description: lines
        data = {}
        for line in fm_text.splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                data[k.strip()] = v.strip().strip('"').strip("'")
    if not isinstance(data, dict):
        return None, "frontmatter is not a YAML mapping"
    return data, None


def validate_one(path: Path, strict: bool) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8", errors="replace")

    if len(text) > MAX_CONTENT_LEN:
        problems.append(f"content {len(text)} chars > {MAX_CONTENT_LEN}")

    fm, err = parse_frontmatter(text)
    if err:
        problems.append(f"frontmatter: {err}")
        return problems

    name = fm.get("name")
    if not name:
        problems.append("missing 'name'")
    elif not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", str(name)):
        problems.append(f"name '{name}' must be lowercase+hyphens")
    elif len(str(name)) > MAX_NAME_LEN:
        problems.append(f"name {len(str(name))} chars > {MAX_NAME_LEN}")

    desc = fm.get("description")
    if not desc:
        problems.append("missing 'description'")
    else:
        desc_str = str(desc)
        if len(desc_str) > MAX_DESC_LEN:
            problems.append(f"description {len(desc_str)} chars > {MAX_DESC_LEN}")
        if not desc_str.startswith("Use when"):
            problems.append("description should start with 'Use when' (trigger discipline)")

    # recommended (flagged only in --strict)
    if strict:
        for field in ("version", "author", "license"):
            if field not in fm:
                problems.append(f"missing recommended field '{field}'")
        meta = fm.get("metadata")
        if not isinstance(meta, dict):
            problems.append("missing metadata block")
        else:
            hermes = meta.get("hermes")
            if not isinstance(hermes, dict):
                problems.append("missing metadata.hermes")
            else:
                if "tags" not in hermes:
                    problems.append("missing metadata.hermes.tags")
                if "related_skills" not in hermes:
                    problems.append("missing metadata.hermes.related_skills")

    # structure
    if "## Common Pitfalls" not in text:
        problems.append("missing '## Common Pitfalls' section")
    if "## Verification Checklist" not in text:
        problems.append("missing '## Verification Checklist' section")
    if "## Overview" not in text:
        problems.append("missing '## Overview' section")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate skill-arsenal SKILL.md files")
    ap.add_argument("--strict", action="store_true", help="flag missing recommended fields")
    args = ap.parse_args()

    if not SKILLS_DIR.is_dir():
        print(f"FAIL: skills dir not found at {SKILLS_DIR}")
        return 1

    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    if not skill_files:
        print("FAIL: no SKILL.md files found")
        return 1

    total_problems = 0
    for f in skill_files:
        rel = f.relative_to(REPO_ROOT).as_posix()
        problems = validate_one(f, args.strict)
        if problems:
            total_problems += len(problems)
            print(f"FAIL {rel}")
            for p in problems:
                print(f"     - {p}")
        else:
            print(f"ok   {rel}")

    print(f"\n{len(skill_files)} skills, {total_problems} problems")
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
