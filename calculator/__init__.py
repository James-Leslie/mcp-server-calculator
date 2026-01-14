import os
from .server import mcp


def main():
    transport = os.getenv("MCP_TRANSPORT", "stdio")

    if transport == "http":
        try:
            port = int(os.getenv("MCP_PORT", "8000"))
        except ValueError:
            port = 8000
        mcp.run(transport="http", host="127.0.0.1", port=port)
    else:
        mcp.run()  # STDIO by default


if __name__ == "__main__":
    main()
