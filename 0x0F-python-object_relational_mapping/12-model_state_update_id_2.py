#!/usr/bin/python3

"""
A script that changes the name of a State object from the
database
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

    # Retrieve the instance
    instance = session.query(State).filter(State.id == 2).one()

    # Update the instance and commit changes
    instance.name = "New Mexico"
    session.commit()
