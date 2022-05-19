from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Piyush"}
    posts = [
        {"author": {"username": "Piyush"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Ravi"}, "body": "The new Marvel movie is cool!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
