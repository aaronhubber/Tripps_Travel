from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("user/user_index.html", users=users)


#NEW
@users_blueprint.route("/users/new")
def new_user():
    return render_template("user/new_user.html")


# CREATE
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form["name"]
    new_user = User(name)
    user_repository.save(new_user)
    return redirect("/users")


# EDIT
@users_blueprint.route("/users/<id>/edit")
def edit_users(id):
    user = user_repository.select(id)
    return render_template('user/edit_user.html', user=user)


# UPDATE
@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    name = request.form["name"]
    new_user = User(name, id)
    user_repository.update(new_user)


# DELETE
@users_blueprint.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    user_repository.delete(id)
    return redirect("/users")