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
    language = request.form["language"]
    founded = request.form["founded"]
    new_city = City(name, language, founded)
    city_repository.save(new_city)
    return redirect("/cities")


# # EDIT
# @zombie_types_blueprint.route("/zombietypes/<id>/edit")
# def edit_zombie_type(id):
#     zombie_type = zombie_type_repository.select(id)
#     return render_template('zombie_types/edit.html', zombie_type=zombie_type)


# # UPDATE
# @zombie_types_blueprint.route("/zombietypes/<id>", methods=["POST"])
# def update_zombie(id):
#     name = request.form["name"]
#     zombie_type = ZombieType(name, id)
#     zombie_type_repository.update(zombie_type)


# # DELETE
# @zombie_types_blueprint.route("/zombietypes/<id>/delete", methods=["POST"])
# def delete_zombie(id):
#     zombie_type_repository.delete(id)
#     return redirect("/zombietypes")