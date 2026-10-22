from fastmcp import FastMCP
mcp = FastMCP("financial-mcp-server")

@mcp.tool()
async def my_tool()->str:
    """this is sample tool that returns the strings"""
    return 'result'

if __name__=="__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8089
    )


    