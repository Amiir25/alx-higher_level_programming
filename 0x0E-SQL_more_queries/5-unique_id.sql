-- This SQL query creates a new table with id and name columns and
-- give a default value for id and make it unique.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
