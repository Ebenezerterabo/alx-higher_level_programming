#!/usr/bin/python3

"""
A script that adds the State object "Louisiana" to the database
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

    # Create a new instance
    new_name = State(name="Louisiana", id=6)

    # Add and commit to database
    session.add(new_name)
    session.commit()
    print(f'{new_name.id}')
