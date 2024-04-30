#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a'
from the database
"""

from sys import argv
from sqlalchemy import func
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Main program """

    # Create Database connection
    db_url = "mysql://{}:{}@localhost:3306/{}".\
        format(argv[1], argv[2], argv[3])

    engine = create_engine(db_url)

    # Create sessionmaker to create session object
    Session = sessionmaker(bind=engine)

    # Creating session object for database manipulation
    session = Session()

    # Constructing the query
    query = session.query(State).order_by(State.id.asc()).\
        filter(func.lower(State.name).like('%a%'))

    # Execute the query and get result
    results = query.all()

    # Iterate over rows and print result
    for result in results:
        print(f'{result.id}: ', result.name)
