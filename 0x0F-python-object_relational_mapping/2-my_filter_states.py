#!/usr/bin/python3
"""script that lists all states from database"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
 
    state_name = sys.argv[4]
    mycursor = db.cursor()
    query = "SELECT states.id, name FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(state_name)
    mycursor.execute(query)
    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    mycursor.close()
    db.close()
