# 100X PM Playground — Streamlit Interface (beta)

A local web app for browsing and test-driving the skills behind the 100X PM command system before committing to a full workflow in Claude Code, ChatGPT, or Codex.

**Status:** Streamlit (beta). This is a new feature in flight and we are actively testing and refining it. Feedback is welcome via [GitHub Issues](https://github.com/Johnnnmai/100x-pm-skills/issues).

**Pedagogic goal:** Lower the barrier from “I have heard about this repo” to “I have seen a real skill work in my context.” The beta app remains skill-first, but the public repo front door is now command-first.

## Running Locally

```bash
pip install -r app/requirements.txt
streamlit run app/main.py
```

## What It Is For

- preview skills before installing them globally
- test PM workflows with your own scenario
- compare provider output quality
- rehearse before using the command system in a live project

## Positioning

This beta app is a supporting playground, not the main product surface.

The main 100X PM entrypoint lives in:

- [README.md](../README.md)
- [START_HERE.md](../START_HERE.md)
- [commands/pm-command-center.md](../commands/pm-command-center.md)
