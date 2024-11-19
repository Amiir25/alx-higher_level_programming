-- A query that converts a database, a table and its
-- filed to utf8.

-- Convert the hbtn_0c_0 database to utf8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8
COLLATE utf8_general_ci;

-- Convert the first_table to utf8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8
COLLATE utf8_general_ci;

-- Convert the name filed of first_table to utf8
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8
COLLATE utf8_general_ci;
