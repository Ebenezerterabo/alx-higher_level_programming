#!/usr/bin/python3
""" A script that lists all states with a name starting with
 N (upper) from database """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Main program """
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY'N%' ORDER BY id ASC")

    results = cursor.fetchall()

    for result in results:
        print(result)

    cursor.close()
    db.close()
