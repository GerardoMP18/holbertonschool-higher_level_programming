#!/usr/bin/python3
""" Script that changes the name of a State object from
    the database hbtn_0e_6_usa """


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

    # Update directly to the DB
    state = session.query(State). \
        filter(State.id == 2).update(
            {
                State.name: 'New Mexico'
            }
        )

    # Update with Object
    # state = session.query(State). \
    #   filter(State.id == 2).first()
    # state.name = 'New Mexico'
    # session.add(state)

    session.commit()
