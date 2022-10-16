#!/usr/bin/python3
"""
A simple flask script to start up an app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return hbnb string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_stuff(text):
    """ Return a string with c"""
    if "_" in text:
        text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
