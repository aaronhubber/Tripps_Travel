from db.run_sql import run_sql
from models.location import Location
from models.user import User
from models.location import Location
from models.dream_location import Dream_location
from models.visited_location import Visited_location
import repositories.user_repository as user_repository
import repositories.location_repository as location_repository

def save(dream_location):
    sql = "INSERT INTO dream_locations (user_id, location_id) VALUES (%s, %s) RETURNING id"
    values = [dream_location.user.id, dream_location.location.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    dream_location.id = id


def select_all():
    dream_locations = []
    sql = "SELECT * FROM dream_locations"
    results = run_sql(sql)
    for result in results:
        user = user_repository.select(result["user_id"])
        location = location_repository.select(result["location_id"])
        dream_location = Dream_location(user, location, result["id"])
        dream_locations.append(dream_location)
    return dream_locations


def select(id):
    sql = "SELECT * FROM dream_locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = user_repository.select(result["user_id"])
    location = location_repository.select(result["location_id"])
    dream_location = Dream_location(user, location, result["id"])
    return dream_location


def delete_all():
    sql = "DELETE FROM dream_locations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM dream_locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(dream_location):
    sql = "UPDATE dream_locations SET (user_id, location_id) VALUES (%s, %s)"
    values = values = [dream_location.user.id, dream_location.location.id, dream_location.id]
    run_sql(sql, values)