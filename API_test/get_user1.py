import requests
resp=requests.get("https://reqres.in/api/users/2")

code=resp.status_code

print(resp.json())

