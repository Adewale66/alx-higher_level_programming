-- Lists all the cities of California
SELECT * FROM states WHERE id IN (SELECT state_id FROM cities WHERE state_id = 1 ORDER BY state_id ASC);
