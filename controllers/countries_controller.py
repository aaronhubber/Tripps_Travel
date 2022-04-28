from flask import Blueprint, Flask, redirect, render_template, request
from models.country import Country
import repositories.country_repository as country_repository
countries_blueprint = Blueprint("countries", __name__)

# INDEX
@countries_blueprint.route("/countries")
def country():
    countries = country_repository.select_all()
    return render_template("country/country_index.html", countries=countries)

#NEW
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("country/new_country.html")

# CREATE
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    population = request.form["population"]
    new_country = Country(name, population)
    country_repository.save(new_country)
    return redirect("/countries")

# EDIT
@countries_blueprint.route("/countries/<id>/edit")
def edit_countries(id):
    country = country_repository.select(id)
    return render_template('country/edit_country.html', country=country)

# UPDATE
@countries_blueprint.route("/countries/<id>", methods=["GET", "POST"])
def update_country(id):
    name = request.form["name"]
    population = request.form["population"]
    new_country = Country(name, population, id)
    country_repository.update(new_country)
    return redirect ("/countries")

# DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")