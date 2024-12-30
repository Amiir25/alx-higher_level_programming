#!/usr/bin/python3

"""
2-my_filter_states.py

This module contains a python script that lists the rows of
'states' table whose 'name' maches the argument from 'hbtn_0e_0_usa'
database.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    database_name = sys.argv[3]
    matched_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_passwd,
        db=database_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (matched_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()