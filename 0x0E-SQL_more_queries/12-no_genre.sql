-- Script list all shows containd in hbtn_0d_tvshows , where show_id is null
SELECT TS.title, TSG.genre_id
FROM tv_shows TS
LEFT JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
WHERE TSG.show_id is null
ORDER BY TS.title ASC, TSG.genre_id ASC
