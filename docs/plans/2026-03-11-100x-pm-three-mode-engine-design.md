# 100X PM Three-Mode Engine Design

**Status:** approved for execution

## Goal

Unify the repo around a single product definition:

**100X PM is a market-twin-powered product strategy OS for PMs and founders.**

The product should feel like one engine with three entry modes, not three separate tools:

1. `product audit`
2. `new idea`
3. `long-range vision`

## Core Product Decision

Do not frame 100X PM as a generic idea validator or prompt library.

Frame it as a strategy compiler that turns messy input into product decisions and execution artifacts through a shared pipeline:

`signal harvesting -> persona / market twin building -> OASIS simulation -> strategy synthesis -> PRD / roadmap / agent handoff`

This keeps the system reusable internally while making the external story clearer.

## Positioning

### Primary definition

`100X PM = market-twin-powered product strategy compiler`

### Core promise

- start from rough ideas, existing products, or messy internal context
- use public signals and simulation to reduce ambiguity
- produce product direction, business model choices, channel strategy, and agent-ready execution artifacts

### Canonical line

`Scrape the market. Simulate the users. Compile the strategy.`

## Why OASIS Must Be In The Main Story

OASIS should not be framed as a side integration or future add-on.

It is the simulation layer that makes the product meaningfully different from ordinary PM prompting:

- `Scrapling` provides external market and social evidence
- persona and market-twin building translate signal into simulation inputs
- `OASIS` pressure-tests reactions, objections, and wedge strength
- 100X PM compiles the result into strategic and execution outputs

The story is not "we integrated OASIS."
The story is "we simulate market and user reactions before committing to a direction."

## Entry Modes

### 1. Product Audit

Start from:

- website
- app
- current product
- reviews
- support logs
- competitor pages

Output:

- pain-point map
- hypothesis set
- wedge recommendation
- business model moves
- channel bets
- execution path

This is the best hero flow for launch because the input is concrete and the output is easy to judge.

### 2. New Idea

Start from:

- rough founder idea
- market thesis
- fuzzy PM concept

Output:

- tighter wedge
- business model
- first channel
- strategic narrative
- first PRD
- first roadmap

This is the strongest second-layer founder path.

### 3. Long-Range Vision

Start from:

- scattered docs
- strategy notes
- roadmap sprawl
- fragmented product context

Output:

- 3-5 year product direction
- strategic narrative
- capability map
- phased roadmap

This is valuable but should not be the homepage hero. It should read as a higher-order mode built on the same engine.

## Launch Priority

Externally:

1. lead with `product audit`
2. support with `new idea`
3. position `long-range vision` as advanced / premium

Internally:

- keep all three modes live in the information architecture
- keep the same shared engine underneath
- avoid building separate stacks for each mode

## Lighty Interaction Model

Lighty is not only branding. Lighty is the routing and orchestration guide.

The default interaction should be:

1. classify the request into one of the three modes
2. restate the detected mode and the input type
3. run the shared five-step engine
4. separate strategic outputs from execution outputs
5. end with the next command

Lighty should always feel like the shortest path into the system.

## Information Architecture Changes

### Root repo

The root `README.md` should stop reading like a generic internal AI OS first.
It should explain that the AI OS execution layer exists to power 100X PM and agent-team delivery.

### 100X PM front door

The 100X PM front door should make these three things obvious within one screen:

1. what the product is
2. what the three modes are
3. how the shared engine works

### Command model

- `pm-command-center` remains the routing desk
- `find-winning-direction` becomes the canonical three-mode strategic front door
- downstream commands remain deepening commands, not rival entrypoints

## GitHub Best-Practice Patterns To Apply

Borrow from successful public repos by keeping the front door:

- discovery-first
- skim-friendly
- command-first
- strongly routed
- explicit about outcomes

Patterns to preserve:

- fast start path near the top
- one canonical entry command
- minimal but concrete promises
- table-based situation-to-command mapping
- avoid burying the main workflow under long theory

## Scope For This Pass

Update the highest-leverage front-door files:

- root `README.md`
- `100x-product-managers/README.md`
- `100x-product-managers/START_HERE.md`
- `100x-product-managers/commands/pm-command-center.md`
- `100x-product-managers/commands/find-winning-direction.md`
- `100x-product-managers/app/STREAMLIT_INTERFACE.md`

## Non-Goals For This Pass

- full command-tree rewrite
- pack restructuring
- skill metadata sweep
- architecture-doc refresh across every AI OS file
- implementation of new simulator helpers

Those can follow after the front door is coherent.
