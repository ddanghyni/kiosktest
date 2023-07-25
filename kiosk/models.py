from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

class BaseMenu(Base):
    __abstract__ = True  # This makes sure SQLAlchemy knows that this is an abstract base class
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
class coffee(BaseMenu):
    __tablename__ = "coffee"
class tea(BaseMenu):
    __tablename__ = "tea"
class ade(BaseMenu):
    __tablename__ = "ade"
class smoothie(BaseMenu):
    __tablename__ = "smoothie"
class cake(BaseMenu):
    __tablename__ = "cake"