-- A SQL query that creates new user and grants
-- permissions

-- Create the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
