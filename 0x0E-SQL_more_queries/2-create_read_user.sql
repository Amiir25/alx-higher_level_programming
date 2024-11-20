-- A SQL query that creates a datatbase and a user and gives
-- the user select privilege.

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Give select permission
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
