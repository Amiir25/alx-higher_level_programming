-- This SQL query creates a database and a table
-- in the database

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table
CREATE TABLE IF NOT EXISTS states(
    id
       INT
       UNIQUE
       AUTO_INCREMENT
       NOT NULL
       PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
