#!/usr/bin/python3
"""script that lists all states from database"""

import MySQLdb
import sys

if __name__ = "__main__":
	db = MySQLdb.connect(
		host="localhost",
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3]
	)

	mycursor = db.cursor()
	query = "SELECT * FROM states ORDER BY states.id ASC"
	mycursor.execute(query)
	rows = mycursor.fetchall()

	for row in rows:
		print(row)

	mycursor.close()
	db.close()
