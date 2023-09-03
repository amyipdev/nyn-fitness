import json
from flask import Flask, redirect, send_from_directory

# TODO: check cookies and redirect to login
# TODO: API endpoints

app = Flask(__name__)
config = json.load(open("nyn-conf.json", "r"))


@app.route("/")
def index():
    return redirect("/index.html", code=301)


@app.route("/<path:path>")
def statroutes(path):
    return send_from_directory("svelte/public", path)


if __name__ == "__main__":
    app.run("::", config["port"])
