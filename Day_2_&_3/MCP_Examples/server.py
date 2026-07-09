from mcp.server.fastmcp import FastMCP

print("Starting FastMCP server...")

mcp=FastMCP("Calculate Server")

@mcp.tool()
def add(a:int,b:int):
    return a+b

@mcp.tool()
def get_employee(emp_id:int):
    employees={
        101:"Lakshya Saxena",
        102:"John Doe",
        103:"Amber Gupta"
    }
    return employees.get(emp_id,"Employee not found")

print("Server started...Waiting for client requests...")

if __name__=="__main__":
    mcp.run()