from flask import Blueprint, Flask, redirect, render_template, request
from models.experience import Experience
from models.location import Location
from models.user import User
import repositories.user_repository as user_repository
import repositories.location_repository as location_repository
import repositories.visited_location_repository as visited_location_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

visited_locations_blueprint = Blueprint("visited_locations", __name__)
#INDEX
@visited_locations_blueprint.route ("/visited_locations")
def visited():
    users = user_repository.select_all()
    visited_locations = visited_location_repository.select_all()
    return render_template("visited_location/visited_index.html",users=users, visited_locations=visited_locations)


#display by users
@visited_locations_blueprint.route ("/visited_locations/filter/user", methods = ["POST"])
def display_user():
    user_id = request.form["user_id"]
    users = user_repository.select_all()
    visited_locations=visited_location_repository.select_locations_by_user_id(user_id)
    return render_template ("visited_location/visited_index.html", users= users, visited_locations=visited_locations)




# NEW
@visited_locations_blueprint.route("/visited_locations/new")
def new_visit():
    users = user_repository.select_all()
    locations = location_repository.select_all()
    return render_template("visited_location/new_visited.html", users=users, locations=locations)

# CREATE
@visited_locations_blueprint.route("/visited_locations", methods=["POST"])
def create_visit():
    user_id = request.form["user_id"]
    location_id = request.form["location_id"]
    user = user_repository.select(user_id)
    location = location_repository.select(location_id)
    new_visited = Experience(user, location)
    visited_location_repository.save(new_visited)
    return redirect("/visited_locations")

# EDIT
@visited_locations_blueprint.route("/visited_locations/<id>/edit")
def edit_visited_list(id):
    visited_location = visited_location_repository.select(id)
    users = user_repository.select_all()
    locations = location_repository.select_all()
    return render_template('visited_location/edit_visited.html', visited_location=visited_location, users=users, locations=locations)

# UPDATE
@visited_locations_blueprint.route("/visited_locations/<id>", methods=["POST"])
def visited_location(id):
    user_id = request.form["user_id"]
    location_id = request.form["location_id"]
    user = user_repository.select(user_id)
    location = location_repository.select(location_id)
    update_visited = Experience(user, location, id)
    visited_location_repository.update(update_visited)
    return redirect("/visited_locations")

# DELETE
@visited_locations_blueprint.route("/visited_locations/<id>/delete", methods=["POST"])
def delete_visit(id):
    visited_location_repository.delete(id)
    return redirect("/visited_locations")