---
name: claude-mcp-manager
description: Search, install, configure, update, and remove MCP servers in Claude Code. Can search the official MCP registry to find servers, preferring official/trusted sources and requiring user permission before installing.
---

# MCP Server Management

**IMPORTANT**: After adding, removing, or updating MCP servers, inform the user to **restart Claude Code** for changes to take effect.

**CRITICAL**: Before removing any server, use `AskUserQuestion` to confirm with the user.

## Quick Reference

```bash
# Install
claude mcp add --transport http <name> <url>
claude mcp add --transport stdio <name> -- <command> [args...]

# List/inspect
claude mcp list
claude mcp get <name>

# Remove (confirm with user first!)
claude mcp remove <name>
```

Options must come BEFORE the server name.

## Searching for MCP Servers

When users ask to find or install an MCP server, see [references/search.md](references/search.md) for:
- Official vendor server lookup (always try first)
- MCP Registry API queries (fallback)
- Known official servers table
- User choice template format

**Trust hierarchy**: Official vendor > MCP reference servers > Verified partners > Community

## Adding Servers

### With Environment Variables

The `--env` CLI flag is unreliable with special characters. Instead:

1. Add server without env vars:
   ```bash
   claude mcp add --transport stdio <name> -- npx -y @package/mcp-server
   ```

2. Edit config file to add env vars. See [references/scopes.md](references/scopes.md) for file locations.

### Collect Configuration First

Before installing, check if the server needs API keys or tokens. Use `AskUserQuestion` to collect required values before running install commands.

## Updating Servers

No direct update command exists. Options:

1. **Edit config directly** (preferred for credential changes)
2. **Remove and re-add** (confirm removal with user first)
3. **Use environment variables** for credentials that change often

For OAuth servers (GitHub, Sentry): Run `/mcp` in Claude Code to re-authenticate.

## Removing Servers

⚠️ Always confirm with user via `AskUserQuestion` before removing.

```bash
claude mcp remove <server-name>
```

For project-scoped servers in `.mcp.json`, delete the entry from the file after user confirmation.

## Reference

- **Search and known servers**: [references/search.md](references/search.md)
- **Transport types**: [references/transports.md](references/transports.md)
- **Scopes and config files**: [references/scopes.md](references/scopes.md)
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)

## Scopes Summary

| Scope | Flag | Config Location | Use Case |
|-------|------|-----------------|----------|
| Local | `--scope local` (default) | `~/.claude.json` | Personal dev servers |
| Project | `--scope project` | `.mcp.json` | Team-shared servers |
| User | `--scope user` | `~/.claude.json` | Cross-project tools |

## Environment Variable Syntax

In config files: `${VAR}` or `${VAR:-default}`

## Windows Note

Use `cmd /c` wrapper for npx:
```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```
