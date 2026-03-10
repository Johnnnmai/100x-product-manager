# Design Eval 100X PM Run

## Run Metadata

- Task: AI eval design
- Command: `design-eval`
- Date: 2026-03-10
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `100xpm`

## Input Bundle

- Source files: `commands/design-eval.md`
- Problem statement: design evaluation for an AI post-call brief with risk labels and follow-up suggestions
- Constraints: medium-high trust risk because bad risk labels may mislead a CSM
- Success criteria: pass/fail logic before launch

## Prompt Used

```text
Using commands/design-eval.md:

Design an evaluation plan for an AI feature that creates post-call customer briefs with risk labels and follow-up suggestions.

Risk level is medium-high because wrong risk labels could mislead a customer success manager.

Follow the command exactly.
Define pass/fail criteria, strong cases, red-flag cases, a human review trigger, and a fallback trigger.
```

## Output Artifact

```md
# Eval Plan: Post-call Risk Brief

## Eval objective

Verify that the model can summarize the call accurately, surface only evidence-linked risk cues, and avoid overstating confidence.

## Pass / fail criteria

### Pass

- summary captures the main customer problem, commitment, and next step
- every risk cue maps to transcript evidence
- follow-up recommendation is relevant to what happened on the call
- uncertainty is stated when evidence is mixed

### Fail

- risk cue has no transcript support
- model labels healthy sentiment as churn risk without evidence
- follow-up recommendation invents product facts or customer commitments
- brief sounds certain when transcript evidence is weak or contradictory

## Strong cases

1. clear escalation language from customer
2. transcript with explicit next steps and owner
3. transcript with mixed sentiment where the model should stay cautious

## Red-flag cases

1. transcript quality is low and the model still emits strong risk labels
2. sarcastic or ambiguous customer language gets treated as explicit risk
3. the model recommends actions not supported by the conversation

## Scorecard

- summary accuracy: 1-5
- evidence-linked risk cues: 1-5
- follow-up usefulness: 1-5
- calibration under ambiguity: 1-5

## Human review trigger

Route to human review when:
- transcript quality is poor
- the model emits high-risk language with weak evidence
- the output confidence note indicates uncertainty

## Fallback trigger

If evidence-linked risk quality fails below threshold, suppress risk labels and return summary-only mode until the eval is fixed.
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 7 min
- Time to acceptable draft: 11 min
- Manual edits after first draft: 2 substantive edits

## Notes

- What improved: actual pass/fail logic, red flags, review trigger, fallback mode
- What failed: still needs dataset design later, but the pre-launch eval logic is now concrete
- Should this run count toward the public benchmark: `yes`
