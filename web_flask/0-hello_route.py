#!/usr/bin/python3
# flask application starting
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    ''' default home route '''
    return "Hellow HBNB!"


if __name__ == '__main__':
    ''' everything starts here '''
    app.run(host="0.0.0.0", port=5000, debug=True)
