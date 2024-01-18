#!/usr/bin/python3
""" Lists all states with a name starting with N from the database hbtn_0e_0_usa. Usage: ./1-filter_states.py <mysql username> <mysql password> \ <database name>"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ Check if the correct number of arguments is provided """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    """ Retrieve arguments """
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """ Connect to MySQL server"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    """ Create a cursor object using the cursor() method """
    cursor = db.cursor()

    """ Execute SQL query to get states starting with 'N'"""
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    """ Fetch all rows"""
    rows = cursor.fetchall()

    """ Display results"""
    for row in rows:
        print(row)

    """ Close the cursor and database connection"""
    cursor.close()
    db.close()
