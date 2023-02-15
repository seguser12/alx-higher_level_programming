-- A script tha lists all the cities of california
-- that can be found in the database 'hbtn_0d_usa'

USE hbtn_0d_usa;

SELECT cities.id, cities.name FROM cities, states WHERE states.name = 'California' AND cities.state_id = states.id ORDER BY cities.id ASC;
