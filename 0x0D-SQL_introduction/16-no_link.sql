-- Script that lists all the records in the second_table table of the hbtn_0c_0
-- database with descending scores and without a value in the name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
