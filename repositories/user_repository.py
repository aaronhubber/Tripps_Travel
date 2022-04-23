from db.run_sql import run_sql
from models.location import Location
from models.user import User

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id


def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result["name"], result["id"])
        users.append(user)
    return users


def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = User(result["name"], result["id"])
    return user


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE users SET name = %s WHERE id = %s"
    values = [user.name, user.id]
    run_sql(sql, values) 

# def dream_locations(user):
#     locations = []

#     sql = "SELECT locations.* FROM locations INNER JOIN dream_locations ON dream_location.location_id = locations.id WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql, values)

#     for result in results:
#         location = Location (result['country'], result['city'], result['continent'], result['highlight'], result['id'] )
#         locations.append(location)

#     return locations


# def visited_locations(user):
#     locations = []

#     sql = "SELECT locations.* FROM locations INNER JOIN visited_locations ON visited_location.location_id = locations.id WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql, values)

#     for result in results:
#         location = Location (result['country'], result['city'], result['continent'], result['highlight'], result['id'] )
#         locations.append(location)

#     return locations