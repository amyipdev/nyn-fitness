import json
import base64
import hashlib
import secrets
import datetime
import uuid

from flask import Flask, redirect, send_from_directory, request, jsonify
import mysql.connector

# TODO: check cookies and redirect to login
# TODO: API endpoints

app = Flask(__name__)
config = json.load(open("nyn-conf.json", "r"))


@app.route("/")
def pagebase():
    return redirect("/index.html", code=301)


@app.route("/<path:path>")
def statroutes(path):
    return send_from_directory("svelte/public", path)


@app.route("/api/verify_token")
def api_verify_tokens():
    tk = request.args.get("tk")
    if len(tk) != 128:
        return jsonify({
            "status": False,
            "uuid": ""
        })
    r = _verify_tokens(tk)
    return jsonify({
        "status": len(r) == 36,
        "uuid": r
    })


@app.route("/api/generate_token", methods=["POST"])
def api_generate_token():
    rq = request.get_json()
    if rq["usn"] == "" or rq["pwd"] == "":
        return "Empty value supplied", 500
    conn = _gendbcon()
    curr = conn.cursor()
    curr.execute("select salt, user_uuid "
                 "from user_info "
                 "where username = %s;",
                 (rq["usn"],))
    rs = curr.fetchall()
    if len(rs) == 0:
        return "403 Forbidden - username not found", 403
    hs = _hash_pwd(rq["pwd"], rs[0][0])
    curr.execute("select 1 "
                 "from user_info "
                 "where password_hs = %s "
                 "and user_uuid = %s;",
                 (hs, rs[0][1]))
    if len(curr.fetchall()) == 0:
        return "403 Forbidden - invalid password", 403
    tk = secrets.token_hex(64)
    curr.execute("insert into tokens "
                 "(expiry_date, token, user_uuid) "
                 "values "
                 "(%s, %s, %s);",
                 (datetime.date.today() + datetime.timedelta(days=(30 if rq["long"] else 7)),
                  tk,
                  rs[0][1]))
    conn.commit()
    return jsonify({
        "token": tk,
        "uuid": rs[0][1]
    })


@app.route("/api/create_account", methods=["POST"])
def api_create_account():
    rq = request.get_json()
    if rq["dn"] == "" or rq["usn"] == "" or rq["pwd"] == "":
        return "Empty value supplied", 500
    conn = _gendbcon()
    curr = conn.cursor()
    salt = secrets.token_hex(16)
    phs = _hash_pwd(rq["pwd"], salt)
    uid = uuid.uuid4()
    curr.execute("insert into user_info "
                 "(displayname, password_hs, salt, username, user_uuid) "
                 "values "
                 "(%s, %s, %s, %s, %s);",
                 (rq["dn"], phs, salt, rq["usn"], str(uid)))
    conn.commit()
    return "true", 200


def _gendbcon() -> mysql.connector.MySQLConnection:
    return mysql.connector.connect(user=config["database"]["user"],
                                   password=config["database"]["pwd"],
                                   host=config["database"]["host"],
                                   database=config["database"]["db"],
                                   port=config["database"]["port"])


def _verify_tokens(token: str) -> str:
    conn = _gendbcon()
    curr = conn.cursor()
    curr.execute("select user_uuid "
                 "from tokens "
                 "where token = %s "
                 "and CURDATE() <= expiry_date;", (token,))
    return x[0][0] if len(x := curr.fetchall()) != 0 else ""


def _hash_pwd(pwd: str, salt: str) -> str:
    return base64.b64encode(
        hashlib.pbkdf2_hmac("sha256", pwd.encode("utf-8"), salt.encode("utf-8"), int(6e5))
    ).decode("ascii").strip()


if __name__ == "__main__":
    app.run("::", config["port"])
