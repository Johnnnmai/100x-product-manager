# RoomJoy Learning Loop

## Purpose
Turn every execution cycle into reusable operational knowledge.

The goal is not only to finish RoomJoy.
The goal is to build a reusable method for future micro-SaaS projects.

## What Must Be Captured
Capture only reusable knowledge.
Do not dump random logs.

## Categories of Reusable Knowledge

### 1. Product Decisions
Examples:
- Why we locked scope
- Why we delayed admin
- Why we chose credits before subscriptions
- Why we stopped landing page polish

### 2. Engineering Patterns
Examples:
- Best way to initialize free credits
- Simplest Supabase auth pattern
- Minimal generation status flow
- Reliable Stripe webhook structure

### 3. Execution Patterns
Examples:
- How to structure audit cycles
- How to avoid agent scope creep
- What summary format saves time
- What validations actually catch problems

### 4. Sale Packaging Patterns
Examples:
- What buyers need to see first
- Which screenshots matter most
- What docs reduce buyer friction
- What "good enough" means for a micro-SaaS sale

## Knowledge File Format
Store reusable lessons in /ops/knowledge/ using one file per lesson.

### Template
# Lesson Title

## Context
What task or problem produced this lesson?

## Observation
What happened?

## Principle
What general rule should be reused later?

## Action Pattern
What should future agents do when similar conditions appear?

## Anti-pattern
What should future agents avoid?

## Reusability
Where else can this apply?

## Good Examples
[List files, flows, or patterns]

## Bad Examples
[List mistakes or dead ends]

## Status
[Draft / Adopted / Deprecated]

## When To Write a New Lesson
Write a lesson only if:
- it saves future time,
- it prevents repeated mistakes,
- it can apply beyond a single small bug.

## When NOT To Write a Lesson
Do not create lessons for:
- trivial one-off bugs
- random logs
- purely temporary environment glitches
- non-reusable styling preferences
