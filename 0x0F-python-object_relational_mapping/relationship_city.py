#!/usr/bin/python3
""" Creation of class City """


from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """ Creation of city model"""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
