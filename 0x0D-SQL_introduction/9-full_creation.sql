-- A SQL query to create a new table and insert
-- records
CREATE TABLE IF NOT EXIST second_table(
    id INT AUTO_INCREMENT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (name, score)
VALUES
    ("John", 10),
    ("Alex", 3),
    ("Bob", 14),
    ("George", 8);
