#HTTP

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1.Let's make a FASTAPI app (that means API) first

app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply(a: float, b: float):
    """ multiply two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the product of the two numbers
    """
    result =  a * b
    return {"result": result}

@app.post("/add")
def add(a: float, b: float):
    """ add two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the sum of the two numbers
    """
    result = a + b
    return {"result": result}

@app.post("/subtract")
def subtract(a: float, b: float):  
    """ subtract two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the difference of the two numbers
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
def divide(a: float, b: float):    
    """ divide two numbers

    args: a(float) : first number
          b(float) : second number

    returns: the quotient of the two numbers
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return {"result": result}


#2.Converting it to MCP
mcp = FastApiMCP(app, name="Calculator MCP")
mcp.mount()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
