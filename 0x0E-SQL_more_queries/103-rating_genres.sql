-- Script to list the list of genres with the sum of rating
SELECT TG.name, SUM(TSR.rate) AS rating
FROM tv_genres TG
INNER JOIN tv_show_genres TSG
ON TG.id = TSG.genre_id
INNER JOIN tv_show_ratings TSR
ON TSG.show_id = TSR.show_id
GROUP BY TG.name
ORDER BY rating DESC;
