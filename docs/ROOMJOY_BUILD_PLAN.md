# RoomJoy Build Plan

## Product Goal
Build RoomJoy into a lightweight, polished, sellable micro-SaaS for AI virtual staging.

The goal is not to build the final company.
The goal is to build a product that:
1. works end to end,
2. looks trustworthy,
3. can charge money,
4. can be handed over to a buyer,
5. can reasonably be listed for sale as a small SaaS asset.

## Product Positioning
RoomJoy helps real estate agents, hosts, and property marketers turn empty room photos into clean, listing-ready staged images in minutes.

## Core Promise
Make empty rooms feel move-in ready.

## Primary Users
1. Real estate agents
2. Airbnb hosts
3. Property marketers
4. Small property managers

## v1 Success Criteria
RoomJoy v1 is considered sellable when all of the following are true:

### Product
- User can sign up and sign in
- User gets free starter credits
- User can upload a room photo
- User can choose room type and style
- User can trigger generation
- User can view result
- User can download result
- User can see project history

### Monetization
- Pricing page exists
- Credits logic exists
- Stripe checkout works for at least one paid plan
- Credits update correctly after payment

### Admin and Transferability
- Basic admin page exists
- README exists
- .env.example exists
- Deployment steps are documented
- Buyer handover summary exists

### Quality
- Build passes
- No major console errors on key pages
- Landing page not broken
- App flow not broken on desktop
- Mobile layout is not obviously broken

## Non-goals
Do not build the following in v1:
- team accounts
- white-label
- affiliate program
- blog/CMS
- custom AI prompt builder
- furniture removal workflow
- multi-language
- advanced analytics
- referral system
- collaboration features
- custom style training

## Tech Stack
- Frontend: Next.js
- UI: Tailwind + shadcn/ui
- Auth: Supabase Auth
- DB: Supabase Postgres
- Storage: Supabase Storage
- Payments: Stripe
- Email: Resend or equivalent
- Generation layer: provider abstraction with one initial provider
- Deployment: Tencent Cloud preview or equivalent
- Execution automation: OpenClaw
- Main code reasoning agent: Claude Code

## Phase Plan

### Phase 1
Auth, user table, free credits initialization, protected app shell

### Phase 2
Upload flow, project creation, room type and style selection

### Phase 3
Generation workflow, result page, download, project history

### Phase 4
Credits, Stripe checkout, plan logic

### Phase 5
Admin page, docs, handover assets, sale packaging

## Rules
1. Do not redesign the landing page unless explicitly requested
2. Do not add scope outside v1
3. Prefer simple maintainable code over clever architecture
4. Every task must include:
   - implementation plan
   - success criteria
   - QA checklist
5. Every execution cycle must produce:
   - one audit summary
   - one delivery summary
6. Every completed task must update:
   - TASK_BOARD.md
   - ops/reports/
   - ops/knowledge/ if a reusable lesson was learned
