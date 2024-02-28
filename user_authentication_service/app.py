#!/usr/bin/env python3
"""
Flask APP
"""
from flask import Flask, jsonify, abort, request, redirect
from flask_cors import (CORS, cross_origin)
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound



app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def get_request() -> str:
    """ get request """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """ register method """
    try:
        AUTH.register_user(request.form["email"], request.form["password"])
        return jsonify({"email": request.form['email'],
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """ login """
    try:
        log = AUTH.valid_login(request.form["email"], request.form["password"])
        if log:
            user_sessionID = AUTH.create_session(request.form["email"])
            response = jsonify({"email": request.form["email"],
                                "message": "logged in"})
            response.set_cookie('session_id', user_sessionID)
            return response
        else:
            return abort(401)
    except ValueError:
        return abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """ logout """
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect("/", 200)
    except NoResultFound:
        return abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
