import sympy
from fastmcp import FastMCP

mcp = FastMCP("Calculator")


@mcp.tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression and return the result.

    Args:
        expression: A mathematical expression as a Python arithmetic string
    """
    try:
        result = sympy.sympify(expression)
    except sympy.SympifyError:
        return "Error: Invalid mathematical expression."

    return f"Result: {result}"
