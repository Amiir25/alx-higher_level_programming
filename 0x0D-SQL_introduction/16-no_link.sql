-- A query that lists all records of the second_table order by
-- score excluding rows with out name value.
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
