# Calculator MCP Server

A simple Python MCP server that provides basic calculator functions.

## Operations

- `add(a: int, b: int)` - Adds two numbers
- `multiply(a: int, b: int)` - Multiplies two numbers

## Configuration
Add to Cursor by updating your MCP configuration:

```json
"calculator": {
  "command": "uvx",
  "args": ["~/mcp-servers/calculator/."]
}
```

Place this in:
- `~/.cursor/mcp.json` for global access
- `.cursor/mcp.json` for project-specific access
