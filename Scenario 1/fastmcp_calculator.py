#libraries
from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """ multiply two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the product of the two numbers
    """
    return a * b

@mcp.tool(
    name = "add",
    description = "Add two numbers",
    tags = ["math", "arithmetic"]
)

def add(a: float, b: float) -> float:
    """ add two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the sum of the two numbers
    """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """ subtract two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the difference of the two numbers
    """
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """ divide two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the quotient of the two numbers
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    mcp.run() #run  the mcp
    #STDIO by default
    