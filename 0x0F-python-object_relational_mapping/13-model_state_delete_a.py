#!/usr/bin/python3

"""
A script that deletes all State objects with a name containing
the letter 'a' from the database
"""

from sys import argv
from model_state import Base, State
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

    # Retrieve the instances with 'a'
    instances = session.query(State).filter(State.name.like('%a%'))

    # loop through the query instances and delete them and commit changes
    for instance in instances:
        session.delete(instance)
    session.commit()
