from flask import Blueprint, Flask, redirect, render_template, request

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