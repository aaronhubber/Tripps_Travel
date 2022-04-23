from flask import Blueprint, Flask, redirect, render_template, request
from controllers.cities_controller import city

from models.location import Location
import repositories.location_repository as location_repository

from models.country import Country
import repositories.country_repository as country_repository

from models.city import City
import repositories.city_repository as city_repository

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route ("/locations")
def location():
    locations = location_repository.select_all()
    return render_template("location/location_index.html", locations=locations)

# NEW
@locations_blueprint.route("/locations/new")
def new_bite():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("location/new_location.html",countries=countries, cities=cities)

# CREATE
@locations_blueprint.route("/locations", methods=["POST"])
def create_location():
    country_id = request.form["country_id"]
    city_id = request.form["city_id"]
    continent = request.form["continent"]
    highlight = request.form["highlight"]
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    location = Location(country, city, continent, highlight)
    location_repository.save(location)
    return redirect("/locations")

# EDIT
@locations_blueprint.route("/locations/<id>/edit")
def edit_location(id):
    locations = location_repository.select(id)
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template('location/edit_location.html', location=locations, countries=countries, cities=cities)

# UPDATE
@locations_blueprint.route("/locations/<id>", methods=["POST"])
def update_locations(id):
    country_id = request.form["country_id"]
    city_id = request.form["city_id"]
    continent = request.form["continent"]
    highlight = request.form["highlight"]
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    location = Location(country, city, continent, highlight, id)
    location_repository.update(location)
    return redirect("/locations")

# DELETE
@locations_blueprint.route("/locations/<id>/delete", methods=["POST"])
def delete_location(id):
    location_repository.delete(id)
    return redirect("/locations")
