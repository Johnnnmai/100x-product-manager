# 100X PM Front Door Convergence Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reframe the repo around the approved 100X PM three-mode engine, with OASIS as a core simulation layer and Lighty as the routing guide.

**Architecture:** Keep one shared strategy engine with three entry modes. Update only the highest-leverage front-door docs and routing commands so the product reads consistently before any deeper skill-tree refactor.

**Tech Stack:** Markdown docs, command docs, repository information architecture, Lighty routing model.

---

### Task 1: Lock The Root Product Story

**Files:**
- Modify: `README.md`

**Step 1: Rewrite the opening positioning**

Replace the current AI OS-first opening with language that makes 100X PM the product surface and the AI OS the execution substrate.

**Step 2: Make OASIS a core layer**

Change references that describe `OASIS / MiroFish` as reserved or second-stage into language that explains simulation as a core differentiator.

**Step 3: Add the shared engine**

Add the five-step chain:

`signal harvesting -> persona / market twin -> OASIS simulation -> strategy synthesis -> PRD / roadmap / agent handoff`

**Step 4: Verify**

Run:

```bash
rg -n "OASIS|100X PM|strategy" README.md
```

Expected:

- root README clearly mentions 100X PM
- OASIS is no longer described as only reserved / mock

### Task 2: Tighten The 100X PM Homepage

**Files:**
- Modify: `100x-product-managers/README.md`

**Step 1: Keep one engine, three modes**

Rework the hero and opening sections so the product reads as one engine with three entry modes.

**Step 2: Strengthen the hierarchy**

Keep all three modes visible, but make `product audit` read like the hero entrypoint and `new idea` / `long-range vision` read as second and third paths.

**Step 3: Add a clear engine visual in text**

Add a compact text or table treatment showing:

`signals -> personas -> simulation -> strategy -> execution`

**Step 4: Tighten output promises**

Make outputs concrete: wedge, business model, channel, PRD, roadmap, agent handoff.

**Step 5: Verify**

Run:

```bash
rg -n "Audit|Shape|Vision|OASIS|Lighty|Scrape the market" 100x-product-managers/README.md
```

Expected:

- all three modes present
- Lighty and OASIS present
- shared engine visible

### Task 3: Rewrite The Guided Start Path

**Files:**
- Modify: `100x-product-managers/START_HERE.md`

**Step 1: Make mode selection the first move**

Ensure the first interaction is explicit routing into audit, shape, or vision.

**Step 2: Show the canonical flow**

Add the shared chain and explain that all three modes reuse it.

**Step 3: Improve the fast-path table**

Keep the "if your situation looks like this" section but make it read like a user decision tree, not a loose command index.

**Step 4: Verify**

Run:

```bash
rg -n "product audit|new idea|long-range vision|signal|simulate|next command" 100x-product-managers/START_HERE.md
```

Expected:

- three-mode routing appears near the top
- shared engine appears once in plain language

### Task 4: Converge The Routing Commands

**Files:**
- Modify: `100x-product-managers/commands/pm-command-center.md`
- Modify: `100x-product-managers/commands/find-winning-direction.md`

**Step 1: Make `pm-command-center` the routing desk**

Tighten it to classify the mode, state the current stage, and route into the shortest useful next command.

**Step 2: Make `find-winning-direction` the unified strategic front door**

Reword it so it clearly supports:

- website / product audit
- rough idea shaping
- messy-context vision synthesis

**Step 3: Separate strategic and execution outputs**

Make the response shape explicit:

- strategic layer
- execution layer
- next command

**Step 4: Verify**

Run:

```bash
rg -n "routing desk|three modes|strategic|execution|next command" 100x-product-managers/commands/pm-command-center.md 100x-product-managers/commands/find-winning-direction.md
```

Expected:

- command center reads like a router
- find-winning-direction reads like one front door, not one narrow use case

### Task 5: Align The Playground Positioning

**Files:**
- Modify: `100x-product-managers/app/STREAMLIT_INTERFACE.md`

**Step 1: Keep the app subordinate**

Make clear the app is a supporting playground, not the main product narrative.

**Step 2: Tie the app to the three-mode system**

Reference Lighty and the three-mode front door so the beta app does not feel detached.

**Step 3: Verify**

Run:

```bash
rg -n "Lighty|three|playground|front door" 100x-product-managers/app/STREAMLIT_INTERFACE.md
```

Expected:

- app doc reads as support surface
- consistent vocabulary with README and START_HERE

### Task 6: Review For GitHub Readability

**Files:**
- Review: `README.md`
- Review: `100x-product-managers/README.md`
- Review: `100x-product-managers/START_HERE.md`
- Review: `100x-product-managers/commands/pm-command-center.md`
- Review: `100x-product-managers/commands/find-winning-direction.md`
- Review: `100x-product-managers/app/STREAMLIT_INTERFACE.md`

**Step 1: Review headings and first-screen scanability**

Check that a GitHub visitor can understand:

- what this is
- who it is for
- how to start
- what the three modes are

within the first screen or two.

**Step 2: Review for duplication**

Remove repeated wording where the same claim is restated too many times across sections.

**Step 3: Review for concrete wording**

Prefer direct language over vague claims like "AI-powered" unless attached to a concrete outcome.

**Step 4: Final verification**

Run:

```bash
git diff -- README.md 100x-product-managers/README.md 100x-product-managers/START_HERE.md 100x-product-managers/commands/pm-command-center.md 100x-product-managers/commands/find-winning-direction.md 100x-product-managers/app/STREAMLIT_INTERFACE.md
```

Expected:

- one coherent product story
- one coherent routing story
- no contradiction between root and 100X PM front doors

**Step 5: Commit**

Do not commit in this workspace unless the user explicitly asks for it, because the repository already contains unrelated uncommitted changes.
