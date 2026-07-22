# Product Analytics 101 workbook

Companion repo for the AI Analyst Lab Lightning Lesson "Product Analytics 101: From Question to
Decision with AI."

It is a small example of an agentic analytics system: metric definitions stored in files, an
analysis workflow that loads when a request matches, and two checkpoints where a person decides
before the system proceeds.

## Contents

```
CLAUDE.md                              project instructions
.claude/skills/analysis-workflow/      the analysis workflow
.claude/commands/                      /frame and /check
.claude/rules/datasets.md              rules that apply when reading data
.claude/hooks/list-datasets.sh         lists available datasets at session start
.claude-plugin/                        manifests that publish this repo as a plugin
datasets/novamart/                     50,000 synthetic users
datasets/storefront/                   50,000 synthetic visitors
```

Each dataset has its own `definitions.md`. No file outside `datasets/` names a dataset, a column, or
a metric. To use your own data, add a folder with a CSV and a definitions file.

## The workflow

```
DECIDE -> ASK -> HYPOTHESIZE -> MEASURE -> VALIDATE -> SHARE -> ACT
```

The workflow stops twice: once before analyzing, to confirm whether the request needs the raw
difference or a causal effect, and once before concluding, to show the comparability check and ask
whether to proceed.

## Run it

Do the walkthrough on the student portal first, in claude.ai, without this repo. The harness here
runs the comparability check immediately, so use it as the second run, not the first.

1. Clone the repo and open it in Claude Code.
2. Paste:

> Users who use Save for Later seem to buy a lot more than users who don't. We're thinking about
> making the Save for Later button more prominent to drive purchases. Should we?

3. It asks whether you want the raw difference or the causal effect. Answer.
4. It measures, runs the comparability check, and stops before concluding.

## The second dataset

`datasets/storefront` has different columns and a different question:

> Desktop visitors order more than mobile visitors. Should we invest in the mobile experience?

The comparability check finds no confound there: the gap holds within every channel, market, and
signup cohort. A check that finds nothing is a valid result.

## Cowork plugin

This repo is also a plugin marketplace.

1. In Claude, open Cowork, then Customize, then Plugins.
2. Choose Add marketplace and enter `ai-analyst-lab/pa101-workbook`.
3. Install `product-analytics`.

The plugin provides the workflow as a skill plus two commands: `frame` (turn a request into a
decision, a question, and a hypothesis) and `check` (run a comparability check on a group
comparison).

## Notes

- The plugin and the project share the same files. `.claude-plugin/plugin.json` points at
  `.claude/skills/` and `.claude/commands/`, so there is one copy of everything.
- Both datasets are synthetic, generated for teaching. No real people, no real company.
