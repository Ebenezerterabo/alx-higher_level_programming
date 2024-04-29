#!/usr/bin/python3

""" A script that prints the first state object from the database """

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine


if __name__ == "__main__":

    # Create engine
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))

    # Create sessionmaker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query state object
    state = session.query(State).order_by(State.id).first()

    # Conditional check
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
