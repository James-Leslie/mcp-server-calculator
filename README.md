# Calculator MCP Server

A simple Python MCP server that provides basic calculator functions.

## Operations

- `calculate(expression: str)` - Evaluates mathematical expressions using sympy
  - **Parameter**: `expression: str` - A mathematical expression string
  - **Returns**: `str` - Result as a string (numeric value or sympy expression)
  - **Supports**: Sympy syntax including operators (`+`, `-`, `*`, `/`, `**`, `^`), functions (`sqrt`, `sin`, `cos`, etc.), and symbols
  - **Example**: `calculate("sqrt(16) + 3**2")` returns `"Result: 13"`
  - **Note**: The previous `add()` and `multiply()` functions have been replaced by this unified calculation tool

## Configuration
Add to Cursor by updating your MCP configuration:

```json
"calculator": {
  "command": "uvx",
  "args": ["--from", "~/mcp-servers/calculator", "mcp-server-calculator"]
}
```

Place this in:
- `~/.cursor/mcp.json` for global access
- `.cursor/mcp.json` for project-specific access
