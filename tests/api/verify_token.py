import requests

print("Test: /api/verify_token")
tk = input("Token: ")
srv = input("IP/Domain: ")

print("VT")
x = requests.get(f"https://{srv}/api/verify_token", params={
    "tk": tk
})
assert x.status_code == 200
print(x.json())
