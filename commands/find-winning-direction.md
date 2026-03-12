# find-winning-direction

Use this when you need one workflow that turns a rough idea or an existing product into a decision pack a founder or PM can act on.

This is **100X PM's primary public workflow**.

It is backed by [../skills/product-direction-compiler/SKILL.md](../skills/product-direction-compiler/SKILL.md).

## Supported Input Modes

1. **Existing product**: website, app, product, reviews, support notes, competitor context
2. **Rough idea**: startup idea, PM thesis, vague wedge, partial constraints

`Long-range vision` is no longer the default public front door for this pass. Treat it as expert mode.

## Input

- a rough idea or an existing product
- optional URLs, notes, reviews, tickets, or support logs
- screenshots, PDFs, decks, docs, or image-based context
- mixed artifact bundles stored locally by the interaction layer
- constraints, if known
- target user or market guess, if known
- risks, goals, or non-goals, if known

The mode is based on the product problem, not on whether the user started with a file, a link, or a screenshot.

## Required Output Contract

Every run should return these sections in order:

1. `Detected input mode`
2. `Given context`
3. `Collected signals` or `Signals unavailable`
4. `Assumptions`
5. `Validated direction`
6. `PRD`
7. `Roadmap`
8. `Agent handoff pack`
9. `Needs validation next`

## Internal Workflow

Use this architecture line exactly when explaining the mechanism:

```text
signal collection -> user/market model -> simulation -> strategy synthesis -> PRD / roadmap / agent handoff
```

`LightCube` names this mechanism layer. `100X PM` remains the public product.

## Operating Rules

- classify the input as `existing product` or `rough idea` before doing anything else
- do not imply live scraping, simulation, or tool execution if it did not actually happen
- separate `Given`, `Collected`, `Simulated inference`, and `Assumed`
- if signals are missing, say `Signals unavailable` and produce a bounded first pass from the provided context only
- if the input is vague, ask for the minimum missing context or give a bounded first-pass output instead of leaking internal syntax
- treat links, screenshots, docs, and notes as one artifact bundle instead of forcing the user to pre-sort inputs
- when a local interface exists, store artifacts locally and treat that local bundle as the working source of truth
- preserve strong pushback on contradictory, impossible, or unsafe premises
- return the full pack every time instead of routing the user through multiple public commands

## What Good Output Looks Like

A good first run should produce:

- one bet worth pursuing
- one PRD draft that matches the bet
- one roadmap that matches the PRD
- one handoff pack that can move into execution
- clear evidence boundaries

## Expert-Mode Follow-Up

If deeper manual follow-up is still needed after the full pack, the main helper commands are:

- `validate-demand`
- `agent-prd`
- `run-roadmap`
