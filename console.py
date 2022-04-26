from models.dream_location import Experience
import repositories.dream_location_repository as dream_location_repository

from models.experience import Experience
import repositories.visited_location_repository as visited_location_repository

from models.user import User
import repositories.user_repository as user_repository

from models.location import Location
import repositories.location_repository as location_repository

from models.city import City
import repositories.city_repository as city_repository

from models.country import Country
import repositories.country_repository as country_repository


dream_location_repository.delete_all()
visited_location_repository.delete_all()
user_repository.delete_all()
location_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

city1 = City("Hangzhou", "temperate")
city_repository.save(city1)

city2 = City ("Boston", "temperate" )
city_repository.save(city2)

city3 = City("Bristol", "temperate")
city_repository.save(city3)

country1 = Country ("China", 1400 )
country_repository.save(country1)

country2 = Country ("USA", 329 )
country_repository.save(country2)

location1 = Location (country1, city1, "Asia")
location_repository.save(location1)

location2 = Location (country2, city2, "North America")
location_repository.save(location2)

user1 = User ("Will Jones")
user_repository.save(user1)
user2 = User ("Charlie Day")
user_repository.save(user2)

dream_location1 = Experience(user1, location1)
dream_location_repository.save(dream_location1)

dream_location2 = Experience (user2, location2)
dream_location_repository.save(dream_location2)

visited_location1 = Experience(user1, location1)
visited_location_repository.save(visited_location1)

visited_location2 = Experience (user2, location2)
visited_location_repository.save(visited_location2)

# print (user_repository.dream_locations(user1))
#print(location_repository.dream_users(location1))
