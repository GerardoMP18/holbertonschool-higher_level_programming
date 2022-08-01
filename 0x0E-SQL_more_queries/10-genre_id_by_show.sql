-- Script that lists all shows contained in hbtn0d_tv_shows
SELECT TS.title, TSG.genre_id
FROM tv_shows TS
INNER JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
ORDER BY TS.title ASC, TSG.genre_id ASC;
