#!/usr/bin/python3
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

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    results = cursor.fetchall()

    for result in results:
        print(result)

    cursor.close()
    db.close()
