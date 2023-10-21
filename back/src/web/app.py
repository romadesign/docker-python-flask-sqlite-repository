# file: src/web/app.py
from flask import Flask, request, abort, send_from_directory
from pathlib import Path
from src.lib.web import create_app, request, create_access_token, json_response

from config import config

# from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


from src.domain.interactor.user_interactor import UserInteractor
from src.domain.repository.user_repository import UserRepository
from src.domain.interactor.test_interactor import TestInteractor
from src.domain.repository.test_repository import TestRepository

app = create_app(config)

user_repository = UserRepository(config)
user_interactor = UserInteractor(config, user_repository)
test_repository = TestRepository(config)
test_interactor = TestInteractor(config, test_repository)


@app.route("/")
def home():
    return "magic ..."

# new test aqui
@app.route("/api/test", methods=["GET"])
def tests_get():
    result = test_interactor.get_all_tests()
    return json_response(result), 200
    

@app.route("/images/<path:filename>", methods=["GET"])
def image(filename):
    return send_from_directory(Path.cwd() / "static", filename)


@app.route("/api/auth/login", methods=["POST"])
def auth_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = user_interactor.auth_user(username, password)
    access_token = create_access_token(identity=user.id)
    return json_response({"access_token": access_token, "user": user}), 200


@app.route("/api/me", methods=["GET"])
def user():
    return json_response({"current_user": user_interactor.get_current_user()}), 200


@app.route("/api/only-for-admin", methods=["GET"])
def only_for_admin():
    return json_response({"current_user": user_interactor.get_current_admin()}), 200


@app.route("/api/users", methods=["GET"])
def get_all_users():
    users = user_interactor.get_all_users()
    return json_response(users), 200


@app.route("/api/users/<id>", methods=["GET"])
def get_users_by_id(id):
    user = user_interactor.get_user_by_id(id)
    return json_response(user), 200


@app.route("/api/users/save_user", methods=["POST"])
def save_user():
    data = request.get_json()
    user_interactor.save_user(data)
    return "", 200