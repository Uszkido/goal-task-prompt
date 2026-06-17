#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_root="${CODEX_HOME:-$HOME/.codex}/skills"
skill_name="goal-task-prompt"

mkdir -p "$target_root"
cp -R "$repo_root/skill/$skill_name" "$target_root/"

echo "Installed $skill_name to $target_root/$skill_name"
echo 'Try: Use $goal-task-prompt turn this rough idea into a verifiable /goal prompt.'

