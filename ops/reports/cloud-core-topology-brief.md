# Cloud Core Topology Brief

## What changed

- Recast the Paperclip fleet so the company control nodes are cloud-backed by default.
- Kept only bounded execution lanes as local fallbacks.
- Updated provisioning so missing OpenClaw roles are reported explicitly instead of being treated like local hires.

## Cloud core roles

- `CEO`
- `Chief of Staff`
- `CTO`
- `QA Director`
- `Research Lead`
- `Growth Lead`

## Local fallback roles

- `Local Codex Builder`
- `Staff Engineer`

## Why

- The control plane must stay alive when the desktop is offline.
- Project ownership should not depend on local shells.
- Local agents should accelerate execution, not define the company topology.

## Verification target

- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/provision_company_portfolio.py --dry-run`

## Blockers

- Cloud-backed roles still require actual OpenClaw onboarding and gateway URLs before they can be live-assigned in Paperclip.
