-- Script to list the show of the genres of name "Comedy"
SELECT TS.title
FROM tv_shows TS
INNER JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
INNER JOIN tv_genres TG
ON TSG.genre_id = TG.id
WHERE TG.name = "Comedy"
ORDER BY TS.title ASC;

