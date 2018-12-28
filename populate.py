from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Order

engine = create_engine('sqlite:///restaurant-online-order.db')

# Bind engine to the metadata of the Base class for DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# changes to database are in staging until session.commit() is called
session = DBSession()

# Sample user 01 with items
user01 = User(name="Sample User01")
session.add(user01)

order01 = Order(user=user01, cost=4.90, lettuce=1, cheese=1, bacon=0, meat=1)
session.add(order01)

# Commit data to database
session.commit()

print("Sample data added...")
