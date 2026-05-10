from mcp.server.fastmcp import FastMCP
from datetime import datetime


mcp = FastMCP("time_server")

@mcp.tool()
async def get_current_datetime() -> str:
    """Get the current date time.

    """
    current_datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return current_datetime_str

if __name__ == "__main__":
    mcp.run(transport='stdio')