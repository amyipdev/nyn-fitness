import json

config = dict()

config["port"] = int(input("Port number: "))

json.dump(config, open("nyn-conf.json", "w"))
