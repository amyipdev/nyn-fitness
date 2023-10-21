import requests

print("Test: /api/create_account")
usn = input("Username: ")
pwd = input("Password: ")
dn = input("Display name: ")
srv = input("IP/Domain: ")

x = requests.post(f"https://{srv}/api/create_account", json={
    "usn": usn,
    "pwd": pwd,
    "dn": dn
})
assert x.status_code == 200
