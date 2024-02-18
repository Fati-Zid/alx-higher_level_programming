#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states from the database hbtn_0e_0_usa.

Usage:
	./0-select_states.py username password database

Arguments:
	username: MySQL username
	password: MySQL password
	database: Database name

The script connects to a MySQL server running on localhost at port 3306 and fetches all states from the database hbtn_0e_0_usa. Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

def list_states(username, password, database):
	"""
	Connect to the MySQL server and list all states from the specified database.

	Args:
		username (str): MySQL username
		password (str): MySQL password
		database (str): Database name

	Returns:
		None
	"""
	try:
		# Connect to MySQL server
		db = MySQLdb.connect(
			host="localhost",
			port=3306,
			user=username,
			passwd=password,
			db=database
		)

		# Create cursor object
		cursor = db.cursor()

		# Execute SQL query
		cursor.execute("SELECT * FROM states ORDER BY id ASC")

		# Fetch all rows
		rows = cursor.fetchall()

		# Print results
		for row in rows:
			print(row)

		# Close cursor and connection
		cursor.close()
		db.close()

	except MySQLdb.Error as e:
		print("MySQL Error:", e)
