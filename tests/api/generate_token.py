import requests

print("Test: /api/generate_token")
usn = input("Username: ")
pwd = input("Password: ")
long = bool(input("Long? (True/False) "))
srv = input("IP/Domain: ")

x = requests.post(f"https://{srv}/api/generate_token", json={
    "usn": usn,
    "pwd": pwd,
    "long": long
})
assert x.status_code == 200
print(x.json())
