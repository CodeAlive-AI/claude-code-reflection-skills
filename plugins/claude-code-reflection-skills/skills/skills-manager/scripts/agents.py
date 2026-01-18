#!/usr/bin/env python3
"""Shared agent definitions for multi-agent skill management.

Supports 15 AI coding agents with their skill directory configurations.
"""

from pathlib import Path
from typing import TypedDict


class AgentConfig(TypedDict):
    """Configuration for an AI coding agent."""
    name: str
    display_name: str
    project_dir: str      # Relative path for project-level skills
    global_dir: str       # Path for user-level skills (supports ~)
    detect_paths: list[str]  # Paths to check for agent installation


# All supported AI coding agents
AGENTS: dict[str, AgentConfig] = {
    "opencode": {
        "name": "opencode",
        "display_name": "OpenCode",
        "project_dir": ".opencode/skill",
        "global_dir": "~/.config/opencode/skill",
        "detect_paths": ["~/.config/opencode"],
    },
    "claude-code": {
        "name": "claude-code",
        "display_name": "Claude Code",
        "project_dir": ".claude/skills",
        "global_dir": "~/.claude/skills",
        "detect_paths": ["~/.claude"],
    },
    "codex": {
        "name": "codex",
        "display_name": "Codex",
        "project_dir": ".codex/skills",
        "global_dir": "~/.codex/skills",
        "detect_paths": ["~/.codex"],
    },
    "cursor": {
        "name": "cursor",
        "display_name": "Cursor",
        "project_dir": ".cursor/skills",
        "global_dir": "~/.cursor/skills",
        "detect_paths": ["~/.cursor"],
    },
    "amp": {
        "name": "amp",
        "display_name": "Amp",
        "project_dir": ".agents/skills",
        "global_dir": "~/.config/agents/skills",
        "detect_paths": ["~/.config/amp"],
    },
    "kilo": {
        "name": "kilo",
        "display_name": "Kilo Code",
        "project_dir": ".kilocode/skills",
        "global_dir": "~/.kilocode/skills",
        "detect_paths": ["~/.kilocode"],
    },
    "roo": {
        "name": "roo",
        "display_name": "Roo Code",
        "project_dir": ".roo/skills",
        "global_dir": "~/.roo/skills",
        "detect_paths": ["~/.roo"],
    },
    "goose": {
        "name": "goose",
        "display_name": "Goose",
        "project_dir": ".goose/skills",
        "global_dir": "~/.config/goose/skills",
        "detect_paths": ["~/.config/goose"],
    },
    "gemini-cli": {
        "name": "gemini-cli",
        "display_name": "Gemini CLI",
        "project_dir": ".gemini/skills",
        "global_dir": "~/.gemini/skills",
        "detect_paths": ["~/.gemini"],
    },
    "gemini": {
        "name": "gemini",
        "display_name": "Gemini CLI",
        "project_dir": ".gemini/skills",
        "global_dir": "~/.gemini/skills",
        "detect_paths": ["~/.gemini"],
    },
    "antigravity": {
        "name": "antigravity",
        "display_name": "Antigravity",
        "project_dir": ".agent/skills",
        "global_dir": "~/.gemini/antigravity/skills",
        "detect_paths": ["~/.gemini/antigravity"],
    },
    "github-copilot": {
        "name": "github-copilot",
        "display_name": "GitHub Copilot",
        "project_dir": ".github/skills",
        "global_dir": "~/.copilot/skills",
        "detect_paths": ["~/.copilot"],
    },
    "clawdbot": {
        "name": "clawdbot",
        "display_name": "Clawdbot",
        "project_dir": "skills",
        "global_dir": "~/.clawdbot/skills",
        "detect_paths": ["~/.clawdbot"],
    },
    "droid": {
        "name": "droid",
        "display_name": "Droid",
        "project_dir": ".factory/skills",
        "global_dir": "~/.factory/skills",
        "detect_paths": ["~/.factory/skills"],
    },
    "windsurf": {
        "name": "windsurf",
        "display_name": "Windsurf",
        "project_dir": ".windsurf/skills",
        "global_dir": "~/.codeium/windsurf/skills",
        "detect_paths": ["~/.codeium/windsurf"],
    },
}


def get_agent_config(agent: str) -> AgentConfig | None:
    """Get configuration for an agent by ID.

    Args:
        agent: Agent ID (e.g., "claude-code", "cursor")

    Returns:
        AgentConfig if found, None otherwise
    """
    return AGENTS.get(agent)


def validate_agent(agent: str) -> bool:
    """Check if an agent ID is valid.

    Args:
        agent: Agent ID to validate

    Returns:
        True if valid, False otherwise
    """
    return agent in AGENTS


def list_all_agents() -> list[AgentConfig]:
    """Return all supported agent configurations.

    Returns:
        List of all agent configs
    """
    return list(AGENTS.values())


def get_project_skills_dir(agent: str, cwd: Path | None = None) -> Path | None:
    """Get the project-level skills directory for an agent.

    Args:
        agent: Agent ID
        cwd: Working directory (defaults to current directory)

    Returns:
        Path to project skills directory, or None if agent not found
    """
    config = get_agent_config(agent)
    if not config:
        return None

    base = cwd or Path.cwd()
    return base / config["project_dir"]


def get_global_skills_dir(agent: str) -> Path | None:
    """Get the global (user-level) skills directory for an agent.

    Args:
        agent: Agent ID

    Returns:
        Path to global skills directory, or None if agent not found
    """
    config = get_agent_config(agent)
    if not config:
        return None

    return Path(config["global_dir"]).expanduser()


def detect_installed_agents() -> list[str]:
    """Detect which AI agents are installed on this system.

    Checks for the existence of agent-specific directories.

    Returns:
        List of installed agent IDs
    """
    installed = []

    for agent_id, config in AGENTS.items():
        for detect_path in config["detect_paths"]:
            path = Path(detect_path).expanduser()
            if path.exists():
                installed.append(agent_id)
                break

    # Remove duplicates while preserving order (gemini-cli and gemini share detection)
    seen = set()
    unique = []
    for agent in installed:
        if agent not in seen:
            seen.add(agent)
            unique.append(agent)

    return unique


def get_skills_dir(agent: str, scope: str, cwd: Path | None = None) -> Path | None:
    """Get the skills directory for an agent and scope.

    Args:
        agent: Agent ID
        scope: "project" or "global"
        cwd: Working directory for project scope

    Returns:
        Path to skills directory, or None if agent not found
    """
    if scope == "project":
        return get_project_skills_dir(agent, cwd)
    elif scope == "global":
        return get_global_skills_dir(agent)
    return None
