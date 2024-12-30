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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_passwd,
        db=database_name
    )

    cursor = db.cursor()
    state_name_escaped = MySQLdb.escape_string(state_name).decode()
    query = (
        "SELECT cities.id, cities.name "
        "FROM cities "
        "JOIN states "
        "ON cities.state_id=state.id"
        "WHERE cities.state_id='{}'.id "
        "ORDER BY cities.id"
    ).format(state_name_escaped)
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()
