---
name: analysis-workflow
description: Use when a request asks to compare groups of users, or asks whether to promote, build, fund, or prioritize something based on data. Runs the framing gate, the measurement, the comparability check, and the validation gate.
---

# Analysis workflow

Six steps. Two of them are gates where you stop and wait for a person.

## 1. Load the definitions

Find the dataset in `datasets/` that the request is about. Read its `definitions.md`. Those
definitions are the record. Restate the one you are using when you quote any number.

If there is no `definitions.md`, state the assumptions you are making before you analyze, and ask for
correction.

## 2. Gate 1, framing. Stop here.

If the request implies a decision, ask exactly this and wait:

> Do you want the raw difference between these groups, or the effect the thing actually causes?
> A decision like this needs the causal one. Which do you want?

If they choose the raw difference, say plainly that it will not support the decision, and ask them to
confirm before continuing.

## 3. Measure

Compute the comparison using the loaded definitions. Report the number with its definition beside it.

## 4. The comparability check. Run this without being asked.

People end up in groups for reasons, and those reasons often explain the outcome better than the
thing being studied.

1. Identify variables fixed **before** the behaviour under study. Anything set at signup, assignment,
   or acquisition is fair game. Anything measured afterwards is contaminated and cannot be used as
   evidence about what came before.
2. Compare the groups on each of those.
3. Bucket the population on the one that differs most, recompute inside each bucket, and report the
   raw gap next to the within-bucket gap.

**Cumulative outcomes always need this.** An outcome phrased as "ever did X", with no time window,
accrues with exposure time, so any group that has existed longer wins on it regardless of the thing
being studied.

**Report honestly either way.** If the gap collapses, say the raw comparison was mostly the confound.
If the gap survives in every bucket, say that too. A check that finds nothing is a real result, not a
failed check.

Controlling for a known confound in observational data is not a causal estimate. It tells you whether
the raw comparison can be trusted. It does not tell you the true effect. Only a randomized test does.

## 5. Gate 2, validation. Stop here.

Show what the check found, then ask exactly this and wait:

> Here is what the check found. Do you want me to state a conclusion on this basis?

## 6. Conclude

Three things, in order:

1. The raw number, and which definition produced it.
2. What the comparability check changed, or did not.
3. What would actually settle the question.

If the evidence does not support the decision, say that it does not support it and that a test would
be needed. That is different from saying the thing does not work. Do not overclaim in either
direction.
