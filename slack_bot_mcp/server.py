# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Welcome to FastMCP 🚀"

if __name__ == "__main__":
    # Run with HTTP transport for web deployment
    mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp")