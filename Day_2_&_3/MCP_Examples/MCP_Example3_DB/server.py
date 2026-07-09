from mcp.server.fastmcp import FastMCP
from db import get_all_employees
from db import get_employee_by_department

mcp=FastMCP("EmployeeDB")

@mcp.tool()
def list_employees():

    return get_all_employees()

@mcp.tool()
def employees_by_department(department:str):

    return get_employee_by_department(department)


if __name__ =="__main__":
    mcp.run()