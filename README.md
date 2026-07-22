# Product Analytics 101 — workbook

Companion repo for the AI Analyst Lab Lightning Lesson *Product Analytics 101: From Question to
Decision with AI*.

It contains a synthetic dataset and a small harness that makes an AI analyst follow a workflow
instead of answering the first question you ask it.

## What's here

- `data/novamart_users.csv` — 50,000 synthetic users, one row each. No real people, no real company.
- `CLAUDE.md` — the harness. Metric definitions, two human gates, and a confound check that runs
  whether or not you remember to ask for it.

## The six steps

```
DECIDE  ->  ASK  ->  HYPOTHESIZE  ->  MEASURE  ->  SHARE  ->  ACT
```

Most analysis is just measure and share. The other four are what turn a number into a decision.

## Two ways to run it, and the order matters

The workflow in this repo is the *second* run. It has the definitions and the checks already written
down, so it will catch the problem in the first step. That is the point of it, and it also spoils the
exercise if you start here.

**Do the walkthrough first, without this repo.** Download the CSV, open
[claude.ai](https://claude.ai), and work through the steps on the student portal. You will get a
clean, correct, confident answer that is about to send you the wrong way. That is the experience the
lesson is built on.

**Then clone this repo and ask the same question.** Open it in Claude Code and paste the request the
way it actually arrives:

> Users who use Save for Later seem to buy a lot more than users who don't. We're thinking about
> making the Save for Later button more prominent to drive purchases. Should we?

It stops and asks what you actually want before it analyzes anything. Answer, and it runs the
comparison, then checks whether the two groups were comparable in the first place, then stops again
before it will state a conclusion.

Same model, same data, same question. The difference is that the definitions live in a file instead
of in your head.

## No install

You don't need this repo. Download the CSV, upload it to claude.ai, and paste the prompts from the
student portal. The workflow is the point, not the tooling.

## The data

Synthetic, generated for teaching. The trap in it is a real one you will hit on real data.
