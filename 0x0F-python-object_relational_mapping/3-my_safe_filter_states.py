#!/usr/bin/python3
""" A script that takes in arguments and displays all values
in the states table of database """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306
    )

    # Create cursor object
    cursor = db.cursor()

    # Query statement
    query = "SELECT * FROM states WHERE name = BINARY %s"
    arg = argv[4]

    # Execute query
    cursor.execute(query, (arg,))

    # Store all filtered input
    results = cursor.fetchall()

    # Print input values from table
    for result in results:
        print(result)

    # Close all process
    cursor.close()
    db.close()
