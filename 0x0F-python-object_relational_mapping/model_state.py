#!/usr/bin/python3

"""
This module contains a class definition of 'State' that inherits
'Base' and is linked to the MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states."""
    __tablename__ = 'states'
    id = Column(
            Integer, primary_key=True, autoincrement=True, nullable=False
        )
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print(
            "Usage: ./6-model_state.py <mysql username>"
            "<mysql password> <database name>"
        )

    else:
        username = argv[1]
        password = argv[2]
        db_name = argv[3]

        # Connect to the MySQL server
        engine = create_engine(
                f'mysql+mysqldb://{username}:{password}@'
                'localhost:3306/{db_name}',
                pool_pre_ping=True
            )

        # Create all tables in the database
        Base.metadata.create_all(engine)
