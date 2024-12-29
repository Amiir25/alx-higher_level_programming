#!/usr/bin/python3

"""
0-select_states.py

This module contains a pyhton script that lists all rows of
'states' table from 'hbtn_0e_0_usa' database.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_passwd,
            db=database_name
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
