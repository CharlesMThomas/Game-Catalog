import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Console(Base):
    __tablename__ = 'console'

    name = Column(String(80), nullable = False)
    picture = Column(String(250))
    id = Column(Integer, primary_key = True)

class Game(Base):
    __tablename__ = 'game'

    name = Column(String(80), nullable = False)
    company = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    picture = Column(String(250))
    cost = Column(Integer, nullable = False)
    description = Column(Text, nullable = False)
    console = relationship(Console)
    console_id = Column(Integer, ForeignKey('console.id'))


engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)