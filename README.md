# Calculator MCP Server
A simple Python MCP server that provides basic calculator functions.

## Operations

- `calculate(expression: str)` - Evaluates mathematical expressions using sympy
  - **Parameter**: `expression: str` - A mathematical expression string
  - **Returns**: `str` - Result as a string (numeric value or sympy expression)
  - **Supports**: Sympy syntax including operators (`+`, `-`, `*`, `/`, `**`, `^`), functions (`sqrt`, `sin`, `cos`, etc.), and symbols
  - **Example**: `calculate("sqrt(16) + 3**2")` returns `"Result: 13"`

## Configuration

Local server:
```json
"calculator": {
  "type": "stdio",
  "command": "uvx",
  "args": ["/path/to/cloned/project"]
}
```

Remote server:
```json
"calculator": {
  "url": "https://mcp-jl-calculator.fastmcp.app/mcp",
  "type": "http"
}
```