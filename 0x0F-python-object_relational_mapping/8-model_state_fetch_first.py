#!/usr/bin/python3
""" Script the prints the first State objects from the
    database hbtn_0e_6usa """


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

    stateFirst = session.query(State).order_by(State.id).first()

    if (stateFirst is None):
        print("Nothing")
    else:
        print("{}: {}".format(stateFirst.id, stateFirst.name))

    session.close()
