from db.run_sql import run_sql
from models.location import Location
from models.city import City
from models.country import Country
from models.experience import Experience
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
from models.user import User
import repositories.user_repository as user_repository

def save(location):
    sql = "INSERT INTO locations (country_id, city_id, continent) VALUES (%s, %s, %s) RETURNING id"
    values = [location.country.id, location.city.id, location.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id


def select_all():
    locations = []
    sql = "SELECT * FROM locations"
    results = run_sql(sql)
    for result in results:
        country = country_repository.select(result["country_id"])
        city = city_repository.select(result["city_id"])
        location = Location(country, city, result["continent"], result["id"])
        locations.append(location)
    return locations


def select(id):
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = country_repository.select(result["country_id"])
    city = city_repository.select(result["city_id"])
    location = Location(country, city, result["continent"], result["id"])
    return location


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(location):
    sql = "UPDATE locations SET (country_id, city_id, continent) = (%s, %s, %s) WHERE id = %s"
    values = values = [location.country.id, location.city.id, location.continent, location.id]
    run_sql(sql, values)

# def dream_users(location):
#     users = []

#     sql = "SELECT users.* FROM users INNER JOIN dream_locations ON dream_locations.user_id = users.id WHERE location_id = %s"
#     values = [location.id]
#     results = run_sql(sql, values)

#     for result in results:
#         user = User(result['name'], result['id'])
#         users.append(user)
#     return users

# def visited_users(location):
#     users = []

#     sql = "SELECT users.* FROM users INNER JOIN visited_locations ON visited_locations.user_id = users.id WHERE location_id = %s"
#     values = [location.id]
#     results = run_sql(sql, values)

#     for result in results:
#         user = User(result['name'], result['id'])
#         users.append(user)
#     return users
