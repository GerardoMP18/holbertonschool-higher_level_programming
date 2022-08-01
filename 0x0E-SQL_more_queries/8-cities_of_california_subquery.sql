-- Script that list all the cities of "California " with the id of table states
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id 
	       	   FROM states
	           WHERE name = "California")
ORDER BY id;
