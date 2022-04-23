from db.run_sql import run_sql
from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, founded, language) VALUES (%s, %s, %s) RETURNING id"
    values = [city.name, city.founded, city.language]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id


def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for result in results:
        city = City(result["name"],result["founded"],result["language"], result["id"])
        cities.append(city)
    return cities


def select(id):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    city = City(result["name"],result["founded"],result["language"], result["id"])
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET name = %s WHERE id = %s"
    values =[city.name, city.founded, city.language,city.id]
    run_sql(sql, values)