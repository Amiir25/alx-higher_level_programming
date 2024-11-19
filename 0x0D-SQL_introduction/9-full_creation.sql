-- A SQL query to create a new table and insert
-- records

-- Create second_table if it's not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserts rows into second_table
INSERT INTO second_table (id, name, score) VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
