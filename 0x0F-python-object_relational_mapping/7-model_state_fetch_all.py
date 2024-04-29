#!/usr/bin/python3

""" A script that lists all state objects from the database """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from sys import argv

if __name__ == "__main__":

    # Create Engine
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))

    # Create sessionmaker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query all states object
    states = session.query(State).order_by(State.id.asc()).all()

    # Print the states
    for state in states:
        print(f'{state.id}:', state.name)

    session.close()
