#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    try:
        """ Connect to MySQL server"""
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        """ Create cursor object"""
        cursor = db.cursor()

        """ Execute SQL query"""
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        """ Fetch all rows"""
        rows = cursor.fetchall()

        """ Print results"""
        for row in rows:
            print(row)

        """ Close cursor and connection"""
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
    
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
