#!/usr/bin/python3
""" List the states that contain the letter a """


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    -------SQL-------
    SELECT * FROM states
    WHERE name LIKE "%a%"
    ORDER BY id
    """

    query = session.query(State). \
        filter(State.name.like("%a%")). \
        order_by(State.id)

    for state in query:
        print("{}: {}".format(state.id, state.name))

    session.close()
