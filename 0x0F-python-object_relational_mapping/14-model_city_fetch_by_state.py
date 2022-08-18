#!/usr/bin/python3
""" Script that prints all the cities with their state
    code and state name"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    ---------- SQL -----------
    SELECT states.name, cities.id, cities.name
    FROM cities
    JOIN states
    WHERE states.id = cities.state_id
    ORDER BY cities.id;
    """

    query = session.query(State, City). \
        join(City). \
        filter(State.id == City.state_id). \
        order_by(City.id).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close
