#!/usr/bin/python3
""" A script that lists all cities from the database """

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

    # Query statements (Combined queries)
    queries = """
    SELECT cities.id, cities.name, states.name AS state_names
    FROM cities JOIN states ON cities.state_id = states.id;
    """

    # Execute iteratively
    cursor.execute(queries)

    # Store results
    results = cursor.fetchall()

    # Print result
    for result in results:
        print(result)

    # Close process
    cursor.close()
    db.close()
