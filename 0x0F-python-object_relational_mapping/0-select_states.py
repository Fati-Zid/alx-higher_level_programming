#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
        cur = db.cursor()

        # Execute query to select all states
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()

        # Print states if there are any
        if rows:
            for row in rows:
                print(row)
        else:
            print()

        # Close cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
