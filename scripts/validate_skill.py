#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "goal-task-prompt"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(path: Path) -> None:
    if not path.exists():
        fail(f"Missing {path.relative_to(ROOT)}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def main() -> None:
    require(SKILL_MD)
    require(OPENAI_YAML)

    text = SKILL_MD.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)

    if fields.get("name") != "goal-task-prompt":
        fail("frontmatter name must be goal-task-prompt")
    if not fields.get("description"):
        fail("frontmatter description is required")
    extra = set(fields) - {"name", "description"}
    if extra:
        fail(f"frontmatter has unsupported fields: {sorted(extra)}")

    line_count = len(text.splitlines())
    if line_count > 500:
        fail(f"SKILL.md should stay under 500 lines, found {line_count}")

    required_phrases = [
        "Goal -> Context -> Inputs -> Boundaries",
        "Stop Conditions",
        "Multi-Agent Goal Orchestration",
        "Quality Check",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"Missing required section or phrase: {phrase}")

    leak_patterns = [
        r"/Users/",
        r"gho_[A-Za-z0-9_]+",
        r"qzt",
        r"iCloud",
    ]
    combined = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.parts and p != Path(__file__).resolve()
    )
    for pattern in leak_patterns:
        if re.search(pattern, combined):
            fail(f"Potential private detail found: {pattern}")

    examples = sorted((ROOT / "examples").glob("*.md"))
    if len(examples) < 4:
        fail("Expected at least 4 examples")

    print("OK: skill package is valid")


if __name__ == "__main__":
    main()
