#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """ displays c + text """
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text):
    """ displays Python + text """
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ displays n is a number if n is an int """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ displays html page """
    return render_template("5-number.html", n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ displays html page """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
