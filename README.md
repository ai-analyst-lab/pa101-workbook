# Product Analytics 101 — workbook

Companion repo for the AI Analyst Lab Lightning Lesson *Product Analytics 101: From Question to
Decision with AI*.

It is a small, deliberately readable example of an agentic analytics system: definitions that live in
files instead of in someone's head, a workflow that runs whether or not you remember it, and two
points where the system stops and makes a person decide.

## What's here

```
CLAUDE.md                              the constraints, 35 lines
.claude/skills/analysis-workflow/      the workflow, loads when a request matches
.claude/rules/datasets.md              constraints that apply when touching data
.claude/hooks/list-datasets.sh         states what datasets exist, every session
datasets/novamart/                     50k synthetic users
datasets/storefront/                   50k synthetic visitors
```

Each dataset carries its own `definitions.md`. Nothing outside `datasets/` names a dataset, a column,
or a metric, so adding your own data means adding a folder and a definitions file, and changing
nothing else.

## The six steps

```
DECIDE  ->  ASK  ->  HYPOTHESIZE  ->  MEASURE  ->  SHARE  ->  ACT
```

Most analysis is just measure and share. The other four are what turn a number into a decision. AI
made a seventh necessary, between measure and share: validate.

## Two ways to run it, and the order matters

The workflow in this repo is the *second* run. The definitions and the checks are already written
down, so it will catch the problem in the first step. That is the point of it, and it also spoils the
exercise if you start here.

**Do the walkthrough first, without this repo.** Download a CSV, open
[claude.ai](https://claude.ai), and work through the steps on the student portal. You will get a
clean, correct, confident answer that is about to send you the wrong way.

**Then clone this and ask the same question.** Open it in Claude Code and paste the request the way
it actually arrives:

> Users who use Save for Later seem to buy a lot more than users who don't. We're thinking about
> making the Save for Later button more prominent to drive purchases. Should we?

It stops and asks what you actually want before it analyzes anything. Answer, and it runs the
comparison, checks whether the two groups were comparable in the first place, and stops again before
it will state a conclusion.

Same model, same data, same question. The difference is where the definitions live.

## Try it on the other dataset

`datasets/storefront` is a different domain with different column names. Ask:

> Desktop visitors order more than mobile visitors. Should we invest in the mobile experience?

Worth doing because the check comes back differently there. A comparability check that finds nothing
is a real result, not a failed one.

## Use it in Cowork

This repo is also a plugin marketplace. In Claude, open Cowork, then **Customize → Plugins → Add
marketplace** and enter:

```
ai-analyst-lab/pa101-workbook
```

Install `product-analytics`. You get the workflow as a skill that fires on its own, plus two
commands: `/product-analytics:frame` to turn a vague request into a decision and a hypothesis, and
`/product-analytics:check` to run a comparability check on a comparison.

The plugin carries no data. Point it at your own.

## A note on the layout

The workflow lives in exactly one file, `product-analytics/skills/analysis-workflow/SKILL.md`.
`.claude/skills/analysis-workflow` is a symlink to it, so cloning the repo and installing the plugin
give you the same workflow and it cannot drift. On Windows, git needs `core.symlinks=true` for that
link to resolve.

## No install

You don't need this repo. Download a CSV, upload it to claude.ai, and paste the prompts from the
student portal. The workflow is the point, not the tooling.
