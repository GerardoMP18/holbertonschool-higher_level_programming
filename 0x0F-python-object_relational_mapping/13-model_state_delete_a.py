#!/usr/bin/python3
""" Script that deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa """


from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

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
    ----SQL----
    DELETE FROM state
    WHERE name like "%a%"
    """

    query = session.query(State). \
        filter(State.name.like("%a%")). \
        all()

    for state in query:
        session.delete(state)

    session.commit()
    session.close()
