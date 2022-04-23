from models.dream_location import Dream_location
import repositories.dream_location_repository as dream_location_repository

from models.visited_location import Visited_location
import repositories.visited_location_repository as visited_location_repository

from models.user import User
import repositories.user_repository as user_repository

from models.location import Location
import repositories.location_repository as location_repository

from models.city import City
import repositories.city_repository as city_repository

from models.country import Country
import repositories.country_repository as country_repository

city1 = City("Hangzhou", 589, "Mandarin")
city_repository.save(city1)

city2 = City ("Boston", 1630, "English" )
city_repository.save(city2)

country1 = Country ("China", 1400000000, "temperate-tropical-arid" )
country_repository.save(country1)

country2 = Country ("USA", 329500000, "temperate-arid-tundra" )
country_repository.save(country2)

location1 = Location (country1, city1, "Asia", "West Lake")
location_repository.save(location1)

location2 = Location (country2, city2, "North America", "Quincy Market")
location_repository.save(location2)

print (location_repository.select(1))