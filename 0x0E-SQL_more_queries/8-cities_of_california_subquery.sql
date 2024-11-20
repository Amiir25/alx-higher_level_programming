-- This SQL query lists all cities of California
-- ordered by cities_id
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
