from flask import Blueprint, Flask, redirect, render_template, request

from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route("/cities")
def city():
    cities = city_repository.select_all()
    return render_template("city/city_index.html", cities=cities)


#NEW
@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("city/new_city.html")


# CREATE
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["name"]
    founded = request.form["founded"]
    language = request.form["language"]
    new_city = City(name, founded, language)
    city_repository.save(new_city)
    return redirect("/cities")


# EDIT
@cities_blueprint.route("/cities/<id>/edit")
def edit_cities(id):
    city = city_repository.select(id)
    return render_template('city/edit_city.html', city=city)


# UPDATE
@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    name = request.form["name"]
    founded = request.form["founded"]
    language = request.form["language"]
    new_city = City(name, founded, language, id)
    city_repository.update(new_city)


# DELETE
@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")