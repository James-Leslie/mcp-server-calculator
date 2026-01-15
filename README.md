# Calculator MCP Server

A Python-based [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that provides mathematical calculation capabilities using [SymPy](https://www.sympy.org/en/index.html). This server enables AI assistants and other MCP clients to perform advanced mathematical computations, from basic arithmetic to symbolic mathematics.

## Usage

### Prerequisites

- **Python 3.12 or higher**
- An MCP client (e.g., [Claude Desktop](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp), [VSCode with Claude extension](https://code.visualstudio.com/docs/copilot/customization/mcp-servers), or any MCP-compatible application)
- Basic familiarity with MCP configuration

Add one of these configurations to your MCP client settings:

### Option 1: Run from GitHub with `uvx`
```json
{
  "calculator": {
    "type": "stdio",
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/James-Leslie/mcp-server-calculator",
      "mcp-server-calculator"
    ]
  }
}
```

### Option 2: Use FastMCP hosted version
```json
{
  "calculator": {
    "type": "http",
    "url": "https://mcp-jl-calculator.fastmcp.app/mcp"
  }
}
```

## Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/James-Leslie/mcp-server-calculator
   cd mcp-server-calculator
   ```

2. **Create a virtual environment** (using uv):
   ```bash
   uv sync
   ```

3. **Run the server**:
   ```bash
   uv run calculator
   ```