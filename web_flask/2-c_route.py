#!/usr/bin/python3
""" moving to end points  """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False
""" JUST EXTRA DOCUMENTATION """

@app.route("/")
def home():
    """ default home route """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """  hbnb end point """
    return "HBNB"


@app.route("/c/<text>")
def info_c(text):
    """ taking argument for displaying c """
    takeout = text.replace("_", " ")
    return f'C {escape(takeout)}'


if __name__ == '__main__':
    # """ everything starts here """
    app.run(host="0.0.0.0", port=5000, debug=True)
