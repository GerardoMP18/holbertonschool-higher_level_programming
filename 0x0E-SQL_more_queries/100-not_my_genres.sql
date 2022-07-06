-- Script to list all genres not linked to the dexte program
SELECT TG.name
FROM tv_genres TG
WHERE TG.name NOT IN (SELECT TG.name
		      FROM tv_genres TG
		      INNER JOIN tv_show_genres TSG
		      ON TG.id = TSG.genre_id
		      INNER JOIN tv_shows TS
		      ON TSG.show_id = TS.id
		      WHERE TS.title = "Dexter")
ORDER BY TG.name ASC;
