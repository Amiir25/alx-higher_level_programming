#!/usr/bin/python3

"""
This module lists all 'State' objects from the database
hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mode_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        usename, password, 3306, database)
    engine = create_engine(connection_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
