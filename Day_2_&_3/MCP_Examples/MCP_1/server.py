from httpcore import __name
from mcp.server.fastmcp import FastMCP
import requests

# print("Starting FastMCP server...")

mcp=FastMCP("Calculate Server")

@mcp.tool()
def get_user(user_id:int):
    url=f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(url)

    if response.status_code == 200:

        user=response.json()

        return f"""
        User Details:
        
        Name              : {user['name']}
        Username          : {user['username']}
        Email             : {user['email']}
        City              : {user['address']['city']}
        Company           : {user['company']['name']}
        """
    else:
        return f"User with ID {user_id} not found."

# print("Server Started........Waiting for client............")
    
if __name__=="__main__":
    mcp.run()












# @mcp.tool()
# def add(a:int,b:int):
#     return a+b

# @mcp.tool()
# def get_employee(emp_id:int):
#     employees={
#         101:"Lakshya Saxena",
#         102:"John Doe",
#         103:"Amber Gupta"
#     }
#     return employees.get(emp_id,"Employee not found")

# print("Server started...Waiting for client requests...")

# if __name__=="__main__":
#     mcp.run()