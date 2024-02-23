#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
 Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
                            <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]))
    [print(state) for state in cursor.fetchall()]
