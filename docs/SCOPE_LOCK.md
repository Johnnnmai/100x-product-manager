# Scope Lock for RoomJoy v1

This document defines what is in scope and what is out of scope.
Agents must obey this document.

## In Scope for v1

### Marketing Site
- navbar
- hero
- gallery
- how it works
- style presets
- use cases
- pricing
- FAQ
- CTA
- footer

### Auth
- sign up
- sign in
- sign out
- protected /app routes

### User Setup
- create user record
- assign 3 free credits

### App Flow
- upload photo
- choose room type
- choose style
- submit generation
- processing/loading state
- result page
- download result
- history page

### Payments
- one-time credits pack and/or one monthly paid plan
- stripe checkout
- webhook update
- credit update logic

### Admin
- view users
- view projects/generations
- basic status visibility

### Docs
- README
- env example
- deploy steps
- buyer handover summary

### Sale Packaging
- screenshots
- short product summary
- feature list
- handover notes

## Out of Scope for v1
- team workspace
- custom prompt builder
- blog
- CMS
- white-label
- multi-language
- advanced analytics
- advanced queue system
- image editor
- furniture removal workflow
- custom style training
- referral or affiliate system
- chat assistant
- marketplace integrations

## Scope Protection Rules
1. Agents may not add new product areas unless explicitly approved
2. Agents may not redesign the landing page while working on backend tasks
3. Agents must prefer the smallest implementation that satisfies the sellable standard
4. Any proposed extra feature must be written under "Future Ideas", not implemented
