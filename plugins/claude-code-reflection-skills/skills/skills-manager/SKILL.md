---
name: skills-manager
description: Lists, inspects, deletes, modifies, moves, and reviews skills for AI coding agents. Use when the user asks to view installed skills, list skills, delete a skill, remove a skill, move skills between scopes, share a skill with the team, edit skill content, review a skill, audit a skill, or improve a skill's quality.
---

# Skills Manager

## Quick Reference

| Task | Command |
|------|---------|
| List all | `python3 scripts/list_skills.py` |
| List by scope | `python3 scripts/list_skills.py -s user` or `-s project` |
| Show details | `python3 scripts/show_skill.py <name>` |
| Review skill | `python3 scripts/review_skill.py <name>` |
| Delete | `python3 scripts/delete_skill.py <name>` |
| Move to user | `python3 scripts/move_skill.py <name> user` |
| Move to project | `python3 scripts/move_skill.py <name> project` |
| Create new | Use `/skill-creator` |
| **Multi-Agent** | |
| Detect agents | `python3 scripts/detect_agents.py` |
| List agent skills | `python3 scripts/list_agent_skills.py --agent cursor` |
| Install to agent | `python3 scripts/install_skill.py /path --agent cursor` |
| Copy between agents | `python3 scripts/copy_skill.py <name> --from claude-code --to cursor` |
| Move between agents | `python3 scripts/move_skill_agent.py <name> --from claude-code --to cursor` |

## Scopes

| Scope | Path | Visibility |
|-------|------|------------|
| User | `~/.claude/skills/` | All projects for this user |
| Project | `.claude/skills/` | This repository only |

User scope takes precedence over project scope for skills with the same name.

## Operations

### List Skills

```bash
python3 scripts/list_skills.py              # All skills
python3 scripts/list_skills.py -s user      # User scope only
python3 scripts/list_skills.py -f json      # JSON output
```

### Show Skill Details

```bash
python3 scripts/show_skill.py <name>           # Basic info
python3 scripts/show_skill.py <name> --files   # Include file listing
python3 scripts/show_skill.py <name> -f json   # JSON output
```

### Review Skill

Audits a skill against best practices and suggests improvements:

```bash
python3 scripts/review_skill.py <name>         # Review with text output
python3 scripts/review_skill.py <name> -f json # JSON output for programmatic use
```

**Checks performed:**
- Name format (lowercase, hyphens, max 64 chars, gerund form)
- Description quality (triggers, third person, specificity)
- Body length (warns if >500 lines)
- Time-sensitive content
- Path format (no Windows backslashes)
- Reference depth (should be one level)
- Table of contents for long files

**After reviewing:** Read the skill's SKILL.md and apply the suggested fixes directly.

### Delete Skill

**CRITICAL**: Always use `AskUserQuestion` to confirm before deleting: "Are you sure you want to delete the skill '[name]'? This cannot be undone."

```bash
python3 scripts/delete_skill.py <name>              # With script confirmation
python3 scripts/delete_skill.py <name> --force      # Skip script prompt
python3 scripts/delete_skill.py <name> -s project   # Target specific scope
```

### Move Skill

```bash
python3 scripts/move_skill.py <name> user      # Project → User (personal)
python3 scripts/move_skill.py <name> project   # User → Project (share with team)
python3 scripts/move_skill.py <name> user -f   # Overwrite if exists
```

### Modify Skill

1. Run `python3 scripts/show_skill.py <name>` to locate it
2. Edit SKILL.md directly at the returned path

### Create New Skill

Use the `/skill-creator` skill for guided creation with proper structure.

## Multi-Agent Operations

Manage skills across 15 supported AI coding agents.

### Supported Agents

| Agent ID | Display Name | Project Skills Dir | Global Skills Dir |
|----------|--------------|-------------------|-------------------|
| `opencode` | OpenCode | `.opencode/skill` | `~/.config/opencode/skill` |
| `claude-code` | Claude Code | `.claude/skills` | `~/.claude/skills` |
| `codex` | Codex | `.codex/skills` | `~/.codex/skills` |
| `cursor` | Cursor | `.cursor/skills` | `~/.cursor/skills` |
| `amp` | Amp | `.agents/skills` | `~/.config/agents/skills` |
| `kilo` | Kilo Code | `.kilocode/skills` | `~/.kilocode/skills` |
| `roo` | Roo Code | `.roo/skills` | `~/.roo/skills` |
| `goose` | Goose | `.goose/skills` | `~/.config/goose/skills` |
| `gemini-cli` | Gemini CLI | `.gemini/skills` | `~/.gemini/skills` |
| `antigravity` | Antigravity | `.agent/skills` | `~/.gemini/antigravity/skills` |
| `github-copilot` | GitHub Copilot | `.github/skills` | `~/.copilot/skills` |
| `clawdbot` | Clawdbot | `skills` | `~/.clawdbot/skills` |
| `droid` | Droid | `.factory/skills` | `~/.factory/skills` |
| `windsurf` | Windsurf | `.windsurf/skills` | `~/.codeium/windsurf/skills` |

### Detect Installed Agents

```bash
python3 scripts/detect_agents.py              # List detected agents
python3 scripts/detect_agents.py --all        # Show all supported agents
python3 scripts/detect_agents.py -f json      # JSON output
```

### List Skills for Any Agent

```bash
python3 scripts/list_agent_skills.py --agent cursor           # Single agent
python3 scripts/list_agent_skills.py --agent goose -s global  # Specific scope
python3 scripts/list_agent_skills.py --all                    # All detected agents
python3 scripts/list_agent_skills.py --agent amp -f json      # JSON output
```

### Install Skill to Agents

```bash
python3 scripts/install_skill.py /path/to/skill --agent cursor              # Single agent
python3 scripts/install_skill.py /path/to/skill --agent cursor --agent amp  # Multiple agents
python3 scripts/install_skill.py /path/to/skill --all                       # All detected
python3 scripts/install_skill.py /path/to/skill --agent goose -s global     # Global scope
python3 scripts/install_skill.py /path/to/skill --agent cursor --force      # Overwrite
```

### Copy Skill Between Agents

```bash
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor --to-scope global
python3 scripts/copy_skill.py my-skill --from claude-code --from-scope project --to amp
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor --force
```

### Move Skill Between Agents

```bash
python3 scripts/move_skill_agent.py my-skill --from claude-code --to cursor
python3 scripts/move_skill_agent.py my-skill --from claude-code --to goose --force
```

## Important Notes

- **Restart required**: After adding, removing, or moving skills, restart the AI agent for changes to take effect
- **Edits are immediate**: Changes to existing skill content work without restart
- **Agent detection**: Uses config directory presence to detect installed agents

## Acknowledgments

Multi-agent support is based on [add-skill](https://github.com/vercel-labs/add-skill) by Vercel Labs.
