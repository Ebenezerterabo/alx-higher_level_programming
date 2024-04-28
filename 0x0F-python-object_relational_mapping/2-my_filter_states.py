#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the
states table of the database """

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

    # Creating cursor object
    cursor = db.cursor()
    # Executing SQL query
    cursor.execute("SELECT * FROM states WHERE name = BINARY'{}'"
                   .format(argv[4]))
    # Fetch the data from the table
    results = cursor.fetchall()

    # print result
    for result in results:
        print(result)

    # Close the process
    cursor.close()
    db.close()
