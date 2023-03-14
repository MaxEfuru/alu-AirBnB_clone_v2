#!/usr/bin/python3
""" moving to end points  """
from flask import Flask
# commenting
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

@app.route('/python/')
@app.route('/python/<text>')
def pythonR(text='is cool'):
    """ python is cool """
    takeout = text.replace("_", " ")
    return "Python {}".format(takeout)


if __name__ == '__main__':
    # """ everything starts here """
    app.run(host="0.0.0.0", port=5000, debug=True)
