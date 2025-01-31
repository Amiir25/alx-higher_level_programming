#!/usr/bin/python3

"""
This module lists all 'State' objects from the database
hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@'
            'localhost:3306/{database}', pool_pre_ping=True
        )

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
