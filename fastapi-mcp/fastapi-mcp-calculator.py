"""FastAPI calculator example exposed as an MCP server.

This module defines a minimal calculator API and mounts it through
`fastapi-mcp` so MCP clients can discover and call the operations.
"""

from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP


app = FastAPI(title="Calculator API")


@app.post("/multiply/")
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


@app.post("/divide/")
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The quotient of the two numbers.

    Raises:
        HTTPException: If the second number is zero.
    """
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    return a / b


@app.post("/add/")
def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


@app.post("/subtract/")
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    return a - b


mcp = FastApiMCP(app, name="Calculator")
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
