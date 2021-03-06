from db.run_sql import run_sql
from models.experience import Experience
import repositories.user_repository as user_repository
import repositories.location_repository as location_repository

def save(visited_location):
    sql = "INSERT INTO visited_locations (user_id, location_id) VALUES (%s, %s) RETURNING id"
    values = [visited_location.user.id, visited_location.location.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    visited_location.id = id



def select_all():
    visited_locations = []
    sql = "SELECT * FROM visited_locations"
    results = run_sql(sql)
    for result in results:
        user = user_repository.select(result["user_id"])
        location = location_repository.select(result["location_id"])
        visited_location = Experience(user, location, result["id"])
        visited_locations.append(visited_location)
    return visited_locations
    

def select_locations_by_user_id(id):
    sql = "SELECT * FROM visited_locations WHERE user_id = %s"
    visited_locations = []
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        user = user_repository.select(result["user_id"])
        location = location_repository.select(result["location_id"])
        visited_location = Experience(user, location, result["id"])
        visited_locations.append(visited_location)
    return visited_locations

def select_locations_by_location_id(id):
    sql = "SELECT * FROM visited_locations WHERE location_id = %s"
    visited_locations = []
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        user = user_repository.select(result["user_id"])
        location = location_repository.select(result["location_id"])
        visited_location = Experience(user, location, result["id"])
        visited_locations.append(visited_location)
    return visited_locations



def select(id):
    sql = "SELECT * FROM visited_locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = user_repository.select(result["user_id"])
    location = location_repository.select(result["location_id"])
    visited_location = Experience(user, location, result["id"])
    return visited_location


def delete_all():
    sql = "DELETE FROM visited_locations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM visited_locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(visited_location):
    sql = "UPDATE visited_locations SET (user_id, location_id) VALUES (%s, %s) WHERE id = %s"
    values = [visited_location.user.id, visited_location.location.id, visited_location.id]
    run_sql(sql, values)