import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states")
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
