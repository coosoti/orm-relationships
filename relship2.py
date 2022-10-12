#!/usr/bin/python3
#
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy import (create_engine)

Base = declarative_base()

engine = create_engine('mysql+mysqldb://root:root@localhost/demo_db', pool_pre_ping=True, echo=True)


class Country(Base):

    __tablename__ = 'countries'

    id = Column(Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='country', cascade='all, delete') # cities belonging to each country


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id')) #id of the country this city belongs to
    country = relationship('Country', back_populates='cities')

Base.metadata.create_all(engine) # create our table
session=sessionmaker()(bind=engine)
