#!/usr/bin/python3

"""
3-my_safe_filter_states.py

This module contains a python script that lists the rows of
'states' table whose 'name' maches the argument from 'hbtn_0e_0_usa'
database, safe from MySQL injection.
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

#    state_name_escaped = MySQLdb.escape_string(state_name).decode()

    query = (
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    ) % state_name
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)

    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()
