#!/usr/bin/python3

"""
5-filter_cities.py

This module contains a python script that takes in name of a
state as an argument and lists all cities of that state.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_passwd,
        db=database_name
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states "
        "ON cities.state_id=state.id"
        "WHERE states.name = %s "
        "ORDER BY cities.id"
    )
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()
