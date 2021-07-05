import requests

resp=requests.get("https://reqres.in/api/users")


code=resp.status_code
assert code == 200, "code doesn't match"


print(resp.json())
print(resp.headers)