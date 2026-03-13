# imports
from fastmcp import FastMCP


mcp = FastMCP(name="Calculator")


# Define tools for basic arithmetic operations
# The @mcp.tool() decorator registers the function as a tool that can be called by the MCP agent.
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


@mcp.tool(
    name="Addition",
    description="Adds two numbers together.",
    tags={"math", "arithmetic"},
)
def add(a: float, b: float) -> float:
    """Adds two numbers together.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


@mcp.tool(
    name="Subtraction",
    description="Subtracts the second number from the first number.",
    tags={"math", "arithmetic"},
)
def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    return a - b


@mcp.tool(
    name="Division",
    description="Divides the first number by the second number.",
    tags={"math", "arithmetic"},
)
def divide(a: float, b: float) -> float:
    """Divides the first number by the second number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The quotient of the two numbers.

    Raises:
        ValueError: If the second number is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # Start the MCP server using HTTP transport. You can also use "websocket" or "grpc" as needed.
    mcp.run(transport="http", host="localhost", port=8080)
