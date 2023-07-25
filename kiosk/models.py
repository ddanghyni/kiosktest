from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


class coffee(Base):
    __tablename__ = "coffee"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

class tea(Base):
    __tablename__ = "tea"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

class ade(Base):
    __tablename__ = "ade"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

class smoothie(Base):   
    __tablename__ = "smoothie"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

class cake(Base):
    __tablename__ = "cake"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

