from typing import Annotated

import sympy
from fastmcp import FastMCP

mcp = FastMCP(
    name="Calculator",
    instructions="""
        A calculator that can evaluate mathematical expressions.
        Call calculate() with a mathematical expression as a string to get the result.
    """,
    website_url="https://github.com/James-Leslie/mcp-server-calculator",
)


@mcp.tool
def calculate(
    expression: Annotated[str, "Python arithmetic expression to evaluate"],
) -> str:
    """Returns the result of a mathematical expression."""
    try:
        result = sympy.sympify(expression)
    except sympy.SympifyError:
        return "Error: Invalid mathematical expression."

    return f"Result: {result}"
