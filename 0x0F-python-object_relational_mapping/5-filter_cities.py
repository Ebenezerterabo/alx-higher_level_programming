#!/usr/bin/python3
""" A script that takes in the name of a state as an argument and
lists all cities of that state, using the database"""

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
    SELECT cities.name FROM cities
    JOIN states on cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    state_name = argv[4]

    # Execute iteratively
    cursor.execute(queries, (state_name,))

    # Store results
    results = cursor.fetchall()

    # Print result
    cities_name = [result[0] for result in results]
outputs = ', '.join(cities_name)
    print(outputs)

    # Close process
    cursor.close()
    db.close()
