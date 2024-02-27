#!/usr/bin/env python3
"""
Flask APP
"""
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

app = Flask(__name__)


@app.route("/", method=['GET'], strict_slashes=False)
def get_request():
    """ get request """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
