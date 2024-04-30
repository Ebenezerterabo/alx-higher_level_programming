#!/usr/bin/python3
"""
A script that prints the State object with the name of passed as
argument from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Main program """

    db_url = "mysql://{}:{}@localhost:3306/{}".\
        format(argv[1], argv[2], argv[3])

    # Create database connection
    engine = create_engine(db_url)

    # Create a sessionmaker to get the session object
    Session = sessionmaker(bind=engine)

    # Create the session object
    session = Session()

    # Construct query
    query = session.query(State).filter_by(name=argv[4])

    # Execute the query
    result = query.first()

    # Print the id or print Not found it it's not found
    if result:
        print(result.id)
    else:
        print("Not found")
