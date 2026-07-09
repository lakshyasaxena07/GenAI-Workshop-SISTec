from mcp.server import FastMCP
from db import get_all_employees
from db import get_employee_by_department

mcp = FastMCP("employee-database")

@mcp.tool()
def get_all_employees():
    return get_all_employees()

@mcp.tool()
def get_employee_by_department(department):
    return get_employee_by_department(department)

if __name__ == "__main__":
    mcp.run()
    
