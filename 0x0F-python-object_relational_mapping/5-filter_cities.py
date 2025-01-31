#!/usr/bin/python3
"""
5-filter_cities.py

This module contains a python script that takes in name of a
state as an argument and lists all cities of that state.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create and execute the SQL query
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all results
    cities = cursor.fetchall()

    # Print the results
    print(", ".join(city[0] for city in cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
