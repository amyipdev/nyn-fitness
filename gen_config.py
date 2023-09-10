import json

config = dict()

config["port"] = int(input("Port number: "))
config["database"] = {
    "host": input("Database IP address: "),
    "port": int(x)
            if (x := input("Database port (leave blank for default): ")) != ""
            else 3306,
    "db": input("Database name: "),
    "pwd": input("Database password: ")
}
config["database"]["user"] = \
    x if \
    (x := input("Database user (if different from name): ")) != "" \
    else config["database"]["db"]

json.dump(config, open("nyn-conf.json", "w"))
