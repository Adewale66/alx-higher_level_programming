-- Lists all the cities of California
SELECT * FROM states WHERE id IN (SELECT id FROM cities WHERE state_id = 1 ORDER BY id ASC);
