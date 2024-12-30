#!/usr/bin/python3

"""
4-cities_by_state

This module contains a python script that lists cities in
states.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_passwd,
        db=database_name
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.name, states.name "
        "FROM states "
        "JOIN cities "
        "ON states.id=cities.state_id "
        "ORDER BY cities.id"
    )
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()
