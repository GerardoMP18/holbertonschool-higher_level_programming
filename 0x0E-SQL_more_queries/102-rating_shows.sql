-- Script to list the shows are the sum of rating in descending order
SELECT TS.title , SUM(TSR.rate) AS rating
FROM tv_shows TS
INNER JOIN tv_show_ratings TSR
ON TS.id = TSR.show_id
GROUP BY TS.title
ORDER BY rating DESC

