-- Script to list the title and name of all programs with their
-- respective show and if a program does not have a genre show null
SELECT TS.title, TG.name
FROM tv_shows TS
LEFT JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
LEFT JOIN tv_genres TG
ON TSG.genre_id = TG.id
ORDER BY TS.title ASC, TG.name ASC
