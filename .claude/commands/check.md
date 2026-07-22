---
description: Run a comparability check on a comparison between two groups, to find out whether the groups were different before the thing being studied.
---

The user has a comparison between groups. Find out whether the groups were comparable to begin with.

1. Read the dataset's `definitions.md` if there is one, and note which columns are fixed before the
   behaviour being studied and which are measured after it. Only the first kind can be used here.
2. Compare the groups on each pre-behaviour variable.
3. Bucket the population on whichever differs most, recompute the comparison inside each bucket, and
   report the raw gap beside the within-bucket gap.

If the outcome is cumulative (an "ever did X" with no time window), always check tenure, because that
kind of outcome accrues with time regardless of the thing being studied.

Report honestly either way. A gap that collapses means the raw comparison was mostly the confound. A
gap that survives in every bucket is a real result, not a failed check.

Say plainly that controlling for a known confound is not a causal estimate. It tells them whether the
raw comparison can be trusted, not what the true effect is.
