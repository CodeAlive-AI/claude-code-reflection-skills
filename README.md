# Claude Code Reflection Skills Plugin

A comprehensive collection of meta-skills for Claude Code that enable self-management and reflection capabilities. These skills allow Claude Code to introspect and modify its own configuration, making it easier to customize and extend the AI assistant's capabilities.

## Included Skills

### claude-skills-manager
List, inspect, delete, modify, and move Claude Code skills between user and project scopes.

### claude-subagents-manager
Create, edit, list, move, and delete Claude Code subagents across user and project scopes.

### claude-plugins-manager
Create, publish, delete, and submit Claude Code plugins. Includes support for plugin marketplaces and official Anthropic directory submission.

### claude-settings-manager
View and configure Claude Code settings.json files across user, project, local, and managed scopes.

### claude-mcp-installer
Search, install, configure, update, and remove MCP servers in Claude Code. Searches the official MCP registry for trusted servers.

### claude-hooks-manager
Manage Claude Code hooks for event-driven automation and custom workflows.

## Installation

Install this plugin using the Claude Code plugin system:

```bash
/plugin marketplace add https://github.com/CodeAlive-AI/claude-code-reflection-skills
/plugin install claude-code-reflection-skills
```

Or install directly from GitHub:

```bash
/plugin install github:CodeAlive-AI/claude-code-reflection-skills
```

## Usage

After installation, the skills will be automatically available to Claude Code. You can invoke them through natural language or by referencing their specific capabilities:

- "List all my installed skills"
- "Show me my Claude settings"
- "Install an MCP server for database access"
- "Create a new subagent for code review"
- "Publish my plugin to GitHub"

## Requirements

- Claude Code CLI
- `gh` CLI (for plugin publishing features)
- Python 3.x (for some skill scripts)

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Author

CodeAlive-AI
