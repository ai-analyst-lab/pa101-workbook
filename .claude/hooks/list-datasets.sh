#!/usr/bin/env bash
# Deterministic: state which datasets exist and where their definitions are, every session,
# so the model never guesses and never silently invents a definition.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
[ -d "$root/datasets" ] || exit 0
echo "Datasets available in this repo:"
for d in "$root"/datasets/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  if [ -f "$d/definitions.md" ]; then
    echo "  - $name (definitions: datasets/$name/definitions.md)"
  else
    echo "  - $name (NO definitions.md, state your assumptions before analyzing)"
  fi
done
echo "Read the definitions file before touching the data."
