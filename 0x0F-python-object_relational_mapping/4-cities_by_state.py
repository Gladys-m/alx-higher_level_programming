#!/usr/bin/python3
"""script that lists all cities from joined tables"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    mycursor = db.cursor()
    query = """
             SELECT cities.id, cities.name, states.name
             FROM cities
             JOIN states ON cities.state_id=states.id
             ORDER BY cities.id ASC
            """
    mycursor.execute(query)
    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    mycursor.close()
    db.close()
