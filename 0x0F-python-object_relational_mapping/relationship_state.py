#!/usr/bin/python3
""" Creation of state model == table state"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class State(Base):
    """ Creacion de state model"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    # Parent = cities, relations One to Many
    cities = relationship("City", backref="state")
