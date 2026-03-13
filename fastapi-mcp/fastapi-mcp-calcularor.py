# imports
from fastapi import FastAPI
# In order to convert a FastAPI app to an MCP server, we need the fastapi_mcp package.
from fastapi_mcp import FastApiMCP 

# Let's make a FastAPI app to serve our calculator tools
app = FastAPI(title="Calculator API")


@app.post("/multiply/")
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    result = a * b
    return result



@app.post("/divide/")
def divide(a: float, b: float) -> float:    
    """Divides the first number by the second number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    result = a / b
    return result


@app.post("/add/")
def add(a: float, b: float) -> float:
    """Adds two numbers together.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    result = a + b
    return result   



@app.post("/subtract/")
def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    result = a - b
    return result

# Now we can convert our FastAPI app to an MCP server using the FastApiMCP class.
mcp = FastApiMCP(app, name="Calculator")
# mcp.mount_http() will mount the MCP server on the FastAPI app, allowing it to handle MCP requests.
# In order to inspect the MCP server, the command `npx @modelcontextprotocol/inspector http://localhost:8000` can be used.
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


