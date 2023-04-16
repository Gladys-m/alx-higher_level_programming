#!/usr/bin/python3
"""script that lists all cities by state"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    state_name = sys.argv[4]
    mycursor = db.cursor()
    query = """SELECT cities.name FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name = %s
             ORDER BY cities.id ASC"""
    mycursor.execute(query, (state_name,))
    rows = mycursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    mycursor.close()
    db.close()
