from flask import Flask, request
from markupsafe import escape
from readyapi import ReadyAPI
from readyapi.middleware.wsgi import WSGIMiddleware

flask_app = Flask(__name__)


@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


app = ReadyAPI()


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


app.mount("/v1", WSGIMiddleware(flask_app))
