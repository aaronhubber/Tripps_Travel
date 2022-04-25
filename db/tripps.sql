DROP TABLE IF EXISTS visited_locations;
DROP TABLE IF EXISTS dream_locations;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    founded INT NOT NULL,
    climate VARCHAR (255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    population INT NOT NULL
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    city_id INT REFERENCES cities(id),
    country_id INT REFERENCES countries(id),
    continent VARCHAR(255),
    highlight VARCHAR(255)
);

CREATE TABLE dream_locations(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    location_id INT REFERENCES locations(id)
);

CREATE TABLE visited_locations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    location_id INT REFERENCES locations(id)
);
