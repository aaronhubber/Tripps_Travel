from flask import Blueprint, Flask, redirect, render_template, request
from controllers.visited_locations_controller import visited_location
from models.location import Location
from models.user import User
from models.experience import Experience
import repositories.user_repository as user_repository
import repositories.location_repository as location_repository
import repositories.dream_location_repository as dream_location_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.visited_location_repository as visited_locations_repository

dream_locations_blueprint = Blueprint("dream_locations", __name__)

@dream_locations_blueprint.route ("/dream_locations")
def dreams():
    dream_locations = dream_location_repository.select_all()
    return render_template("dream_location/dream_index.html", dream_locations=dream_locations)

#New
@dream_locations_blueprint.route("/dream_locations/new")
def new_dream():
    users = user_repository.select_all()
    locations = location_repository.select_all()
    return render_template("dream_location/new_dream.html", users=users, locations=locations)

# CREATE
@dream_locations_blueprint.route("/dream_locations", methods=["POST"])
def create_dream():
    user_id = request.form["user_id"]
    location_id = request.form["location_id"]
    user = user_repository.select(user_id)
    location = location_repository.select(location_id)
    new_dream = Experience(user, location)
    dream_location_repository.save(new_dream)
    return redirect("/dream_locations")

# EDIT
@dream_locations_blueprint.route("/dream_locations/<id>/edit")
def edit_location(id):
    dream_location = dream_location_repository.select(id)
    users = user_repository.select_all()
    locations = location_repository.select_all()
    return render_template('dream_location/edit_dream.html', dream_location=dream_location, users=users, locations=locations)

# UPDATE
@dream_locations_blueprint.route("/dream_locations/<id>", methods=["POST"])
def update_location(id):
    user_id = request.form["user_id"]
    location_id = request.form["location_id"]
    user = user_repository.select(user_id)
    location = location_repository.select(location_id)
    update_dream = Experience(user, location, id)
    dream_location_repository.save(update_dream)
    return redirect("/dream_locations")

# DELETE
@dream_locations_blueprint.route("/dream_locations/<id>/delete", methods=["POST"])
def delete_dream(id):
    dream_location_repository.delete(id)
    return redirect("/dream_locations")

#MOVE
@dream_locations_blueprint.route("/dream_locations/<id>/move")
def move_location(id):
    
    experience = dream_location_repository.select(id)
    dream_location_repository.move_specific(experience)
    
    return redirect("/dream_locations")
