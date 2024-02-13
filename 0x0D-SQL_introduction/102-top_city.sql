-- Displays the top 3 citites temperatures during July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY cit`
ORDER BY avg_temp DESC
LIMIT 3;