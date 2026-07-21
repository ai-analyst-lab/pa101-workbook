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

## Try it

Clone the repo, open it in Claude Code, and ask the question the way it actually arrives:

> Users who use Save for Later seem to buy a lot more than users who don't. We're thinking about
> making the Save for Later button more prominent to drive purchases. Should we?

It will stop and ask you what you actually want before it analyzes anything. Answer, and it will run
the comparison, then check whether the two groups were comparable in the first place, then stop again
before it will state a conclusion.

The short version of what it finds: savers buy at 68.6% against 52.6% for non-savers, a 16-point gap.
Savers have also been customers about 85 days longer, and "buyer" here means *ever placed an order*,
which is cumulative. Compare people who joined around the same time and the gap falls to about 5
points. Most of it was tenure.

## No install

You don't need this repo. Download the CSV, upload it to claude.ai, and paste the prompts from the
student portal. The workflow is the point, not the tooling.

## The data

Synthetic, generated for teaching. The trap in it is a real one you will hit on real data.
