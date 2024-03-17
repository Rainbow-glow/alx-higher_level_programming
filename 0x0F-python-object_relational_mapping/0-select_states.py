#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306
        )
    c = db.cursor()
    c.execute("SELECT * FROM hbtn_0e_0_usa")
    states = c.fetchall()
    for state in states:
        print(f"{state[0]}: {state[1]}")
