#!/usr/bin/env python3
""" Module of Index views
"""
import os
from flask import jsonify, abort, request
from api.v1.views import app_views
from api.v1.views import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ auth sessions login route"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password :
        return jsonify({"error": "password missing"}), 400
    
    user = User.search({"email": email})
    if not user:
        return jsonify({ "error": "no user found for this email" }), 404
    
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    
    from api.v1.app import auth
    session = auth.create_session(user.id)
    SESSION_NAME = os.getenv('SESSION_NAME')

    setCookie = jsonify(user.to_json())
    setCookie.set_cookie(SESSION_NAME, session)

    return setCookie
        