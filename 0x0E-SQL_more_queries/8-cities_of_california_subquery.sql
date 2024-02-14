-- Lists all the cities of California
SELECT * FROM states WHERE id IN (
	SELECT state_id FROM cities WHERE state_id IN (
		SELECT id FROM states WHERE name = 'California'
	) ORDER BY cities.id
);
