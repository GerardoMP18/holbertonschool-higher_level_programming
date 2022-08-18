#!/usr/bin/python3
""" Script that prints the State object with the name
    passed as argument from database hbtn_0e_6_usa """


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
    -----SQL --------
    SELECT id
    FROM states
    WHERE name LIKE "Texas"
    ORDER BY id
    """

    query = session.query(State). \
        filter(State.name.like(argv[4])). \
        order_by(State.id).all()

    if query:
        for state in query:
            print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
