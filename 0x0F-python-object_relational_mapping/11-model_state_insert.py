#!/usr/bin/python3
"""  script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa """


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

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    """
    ----SQL------
    SELECT id
    FROM states
    WHERE name = "Louisiana"
    LIMIT 1
    """

    states = session.query(State). \
        filter(State.name == "Louisiana"). \
        first()

    print("{}".format(states.id))
    session.close()
