# GitHub Skills Best Practices

This note captures the patterns worth borrowing from strong public skills repos reviewed in March 2026.

Repos reviewed:

- [anthropics/skills](https://github.com/anthropics/skills)
- [openai/skills](https://github.com/openai/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [brightdata/awesome-claude-skills](https://github.com/brightdata/awesome-claude-skills)
- [letta-ai/skills](https://github.com/letta-ai/skills)
- [huggingface/skills](https://github.com/huggingface/skills)
- [skillcreatorai/Ai-Agent-Skills](https://github.com/skillcreatorai/Ai-Agent-Skills)

## What Effective Repos Consistently Get Right

### 1. They optimize for discovery before depth

The strongest repos treat `description` as retrieval metadata, not marketing copy.

- Good descriptions say when the skill should load.
- Good descriptions mention the trigger, symptom, or situation.
- Weak descriptions summarize the whole workflow, which makes agents skip the body.

100X PM default:

- Every flagship skill needs a `description`.
- Start with `Use when...`
- Describe the trigger, not the implementation steps.

### 2. They keep the portable core very small

The shared pattern across Anthropic, OpenAI, Hugging Face, Letta, and SkillCreator is simple:

- one folder
- one `SKILL.md`
- optional `scripts/`
- optional `references/`
- optional `assets/` or `examples/`

That simplicity is what makes skills portable across Claude Code, Codex, Letta, Gemini-style loaders, and project-local skill folders.

100X PM default:

- `SKILL.md` is the portable core.
- Repo-specific marketing or long-form explanation belongs in docs, not every skill body.

### 3. They use progressive disclosure

The best large skills stay scannable. They do not dump every rule into one giant markdown file.

Bright Data's larger skills are a good model:

- main workflow in `SKILL.md`
- deeper frameworks in sibling markdown files
- deterministic helpers in `scripts/`
- templates referenced only when needed

100X PM default:

- Keep the main skill easy to scan in one pass.
- Move bulky scorecards, research checklists, or long source notes into `references/` or `examples/`.

### 4. They prefer composable units over mega-skills

Anthropic, OpenAI, Letta, and Hugging Face all organize skills as reusable units that can be composed by a higher-level workflow.

100X PM default:

- `commands/` orchestrate.
- `skills/` specialize.
- Avoid burying three or four jobs inside one giant skill if those jobs can be reused elsewhere.

### 5. They make the first successful run obvious

Popular repos shorten time-to-value with:

- clear install paths
- obvious usage phrasing
- examples
- anti-patterns
- explicit outputs

100X PM default:

- Every flagship skill should show what artifact comes out.
- Every flagship skill should include or reference at least one concrete example.
- Every workflow should make the next recommended skill obvious.

### 6. They make sharing and installation easy

The repos with the strongest ecosystem pull also make skills easy to browse and install from GitHub or a marketplace-style tool.

100X PM default:

- keep `README.md`, `INSTALL.md`, catalog metadata, and file paths aligned
- prefer stable file names and predictable folder layout
- do not advertise commands or packs that do not resolve to real skills

## 100X PM Authoring Defaults

Use these defaults unless there is a strong reason not to:

1. `description` is mandatory on every new flagship skill.
2. `description` should begin with `Use when`.
3. `description` should describe trigger conditions only.
4. `SKILL.md` should hold the minimum reusable workflow.
5. Use `references/` for heavy theory or source notes.
6. Use `scripts/` for deterministic helpers.
7. Use `examples/` for worked scenarios and before/after artifacts.
8. Commands should compose multiple skills instead of duplicating them.
9. Every flagship skill should expose outputs, review checks, and the next logical skill.
10. If a skill cannot be copied into another agent ecosystem without confusion, it is too repo-specific.

## Applied In This Repo

This benchmark has already changed the repo in three concrete ways:

1. Core 100X PM skills now get trigger-first `description` frontmatter.
2. The authoring guides now treat progressive disclosure and portable folder structure as defaults.
3. The guided builder now nudges contributors toward trigger-first descriptions instead of workflow summaries.
