#!/usr/bin/python3

"""
This module contains a class definition of 'State' that inherits
'Base' and is linked to the MySQL table 'states'.
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declaration import declaration_base

Base = declarative_base()


class State(Base):
    """
    This class inherits from base and linked to MySQL table 'states'
    contsaining 'id' and 'name' columns.
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        usename, password, 3306, database
    )
    engine = create_engine(connection_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)
