# Calculator MCP Server

A Python-based [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that provides mathematical calculation capabilities using [SymPy](https://www.sympy.org/en/index.html). This server enables AI assistants and other MCP clients to perform advanced mathematical computations, from basic arithmetic to symbolic mathematics.

## Overview

This MCP server exposes a `calculate` tool that evaluates mathematical expressions using the SymPy library. It supports:

- **Basic arithmetic**: Addition, subtraction, multiplication, division, exponentiation
- **Advanced functions**: Trigonometry, logarithms, square roots, and more
- **Symbolic mathematics**: Work with variables and symbolic expressions
- **Expression parsing**: Natural mathematical syntax with error handling

## Prerequisites

- **Python 3.12 or higher**
- An MCP client (e.g., [Claude Desktop](https://claude.ai/download), [VSCode with Claude extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude), or any MCP-compatible application)
- Basic familiarity with MCP configuration

## Installation

### Quick Start (Using uvx)

The fastest way to use this server is with `uvx`, which runs it directly without installation.

**From GitHub**:
```bash
uvx --from git+https://github.com/James-Leslie/mcp-server-calculator mcp-server-calculator
```

These commands can be used in your MCP client configuration (see [Configuration](#configuration) below).

### From Source (For Development)

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

## Configuration

Add one of these configurations to your MCP client settings:

### Option 1: Run from GitHub with uvx
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

### Option 2: Run from local clone with uv
```json
{
  "calculator": {
    "type": "stdio",
    "command": "uv",
    "args": [
      "--directory",
      "/absolute/path/to/mcp-server-calculator",
      "run",
      "calculator"
    ]
  }
}
```

### Option 3: Use hosted version
```json
{
  "calculator": {
    "type": "http",
    "url": "https://mcp-jl-calculator.fastmcp.app/mcp"
  }
}
```