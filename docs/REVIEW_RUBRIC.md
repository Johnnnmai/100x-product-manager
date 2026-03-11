# Review Rubric for RoomJoy

This rubric is used by AI agents during Audit Mode.
Do not start implementation before completing the review.

## Review Output Format
Every audit must produce:
1. Current status
2. Sellability score /12
3. Per-dimension scores
4. Top 3 blockers
5. Recommended next task
6. Estimated effort
7. Risk if skipped

## Scoring Dimensions

### A. Product Completeness
Check:
- auth exists
- upload exists
- style selection exists
- generation exists
- result page exists
- download exists
- history exists

Score:
0 = missing core loop
1 = partial core loop
2 = complete core loop

### B. Monetization Readiness
Check:
- pricing page exists
- credits model exists
- paid checkout exists
- webhook or payment confirmation updates state

Score:
0 = no working monetization path
1 = partial monetization path
2 = working minimal monetization path

### C. Buyer Transferability
Check:
- README
- env docs
- deploy docs
- admin basics
- handover summary

Score:
0 = poor transferability
1 = partial transferability
2 = clear transferability

### D. UI Polish
Check:
- spacing consistency
- typography consistency
- button consistency
- empty states
- error states
- mobile sanity
- obvious visual breakage

Score:
0 = rough/broken
1 = okay but uneven
2 = polished enough to sell

### E. Technical Stability
Check:
- install works
- build works
- key routes load
- no major runtime blockers
- no severe console errors on key flows

Score:
0 = unstable
1 = partially stable
2 = stable enough for demo and handover

### F. Sale Readiness
Check:
- screenshots
- demo data or demo images
- product summary
- buyer handover materials
- pricing logic visible and believable

Score:
0 = not sale ready
1 = partially packaged
2 = sale ready enough for listing

## Audit Rules
1. Be strict
2. Do not reward incomplete work
3. Recommend only one next task, not five
4. Prefer unblocking the core business loop over polishing
5. Lock marketing page if UI polish already scores 2/2
