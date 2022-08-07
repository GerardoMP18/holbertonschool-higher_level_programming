#!/usr/bin/python3
""" Script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa """


from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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

    createState = State(name="California")
    createCity = City(name="San Francisco")

    createState.cities.append(createCity)

    session.add(createState)
    session.commit()
    session.close()
