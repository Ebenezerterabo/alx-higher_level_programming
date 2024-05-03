#!/usr/bin/python3

"""
A script that prints all city objects from the database
"""

from sys import argv
from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """ Main program """
    # Create the database connection
    db_url = "mysql://{}:{}@localhost:3306/{}".\
        format(argv[1], argv[2], argv[3])

    engine = create_engine(db_url)

    # Activate the sessionmaker to create the session object
    Session = sessionmaker(bind=engine)

    # Create the session object
    session = Session()

    # Construction of query
    query = session.query(City, State).join(State)

    # Execute query
    results = query.all()

    # loop through the query instances and print all objects
    for city, state in results:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
