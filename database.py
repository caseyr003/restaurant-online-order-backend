from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name
        }


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    cost = Column(Float)
    lettuce = Column(Integer)
    cheese = Column(Integer)
    bacon = Column(Integer)
    meat = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'cost': self.cost,
            'user_name': self.user.name,
            'user_id': self.user.id,
            'lettuce': self.lettuce,
            'cheese': self.cheese,
            'bacon': self.bacon,
            'meat': self.meat
        }       


engine = create_engine('sqlite:///restaurant-online-order.db')

Base.metadata.create_all(engine)
