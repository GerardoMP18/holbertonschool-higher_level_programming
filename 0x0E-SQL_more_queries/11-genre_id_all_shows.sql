-- Script that list all show contained in htbn_d_tvshows ,if a show doesn't have a gnre display null
SELECT TS.title, TSG.genre_id
FROM tv_shows TS
LEFT JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
ORDER BY TS.title ASC, TSG.genre_id ASC
