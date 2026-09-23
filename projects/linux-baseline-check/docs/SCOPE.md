# Scope (the “Z” — why this is not a commodity)

## Problem

A student or small team finishes a Linux course and has **no fast way** to see if a box is configured in a risky way (bad file modes, leftover identities, surprise boot services, stale packages).

## Approach

A **small, readable CLI** with a handful of checks that map 1:1 to Linux admin basics (RH024-style): permissions, users/groups, systemd, packages.

## Structural constraint (must stay true)

1. **Teachable** — every check is explainable in one sentence and one command under the hood.  
2. **Local only in v1** — no account, no fleet SaaS.  
3. **Report over reams** — findings a human will actually read in 60 seconds.  
4. **Honest limits** — we do not replace OpenSCAP, Insights, or full CIS benchmarks.

If a competitor already has “scan everything,” our edge is **scoped + documented + student-demoable**, not feature count.
