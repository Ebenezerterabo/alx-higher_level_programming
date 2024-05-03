#!/usr/bin/python3
""" A module that contains the class definition of a city """

from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey

class City(Base):
    """ Structure linked to my sql table """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
