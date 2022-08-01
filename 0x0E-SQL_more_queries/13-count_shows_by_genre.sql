-- Script that list all genres from hbtn_0d_tvshows
SELECT TG.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres TG
INNER JOIN tv_show_genres TSG
ON TG.id = TSG.genre_id
GROUP BY TG.name
ORDER BY number_of_shows DESC;
