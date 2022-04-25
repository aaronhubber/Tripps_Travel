from flask import Flask, render_template

from controllers.dream_locations_controller import dream_locations_blueprint
from controllers.visited_locations_controller import visited_locations_blueprint
from controllers.users_controller import users_blueprint
from controllers.locations_controller import locations_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint

app = Flask(__name__)

app.register_blueprint(dream_locations_blueprint)
app.register_blueprint(visited_locations_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)




@app.route("/")
def main():
    return render_template('index.html')

# @app.route("/search", methods=["POST"])
# def search():
#     pass

if __name__ == '__main__':
    app.run()
