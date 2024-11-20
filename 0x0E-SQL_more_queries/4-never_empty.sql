-- This SQL query creates a new table with id and name
-- columns and give adefault value for id.
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
