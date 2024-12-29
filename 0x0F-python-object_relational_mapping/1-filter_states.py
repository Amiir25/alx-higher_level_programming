#!/usr/bin/python3

"""
1-filter_states.py

This module contains a python script that lists all rows of
'states' table whose 'name' starts with 'N' from 'hbtn_0e_0_usa'
database.
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
    query = "SELECT * FROM states WHERE name LIKE 'A%' ORDER BY id ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
