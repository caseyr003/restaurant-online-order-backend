from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, Item, Order, User

engine = create_engine('sqlite:///restaurant-online-order.db')

# Bind engine to the metadata of the Base class for DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# changes to database are in staging until session.commit() is called
session = DBSession()

# Sample user 01 with items
user01 = User(name="Sample User01")
session.add(user01)

order01 = Order(name="Favorite Order", user=user01, cost=4.90)

lettuce01 = Item(order=order01, name="Lettuce", cost=0.50,
              description="lettuce", )
session.add(lettuce01)
cheese01 = Item(order=order01, name="Cheese", cost=0.30,
              description="cheese")
session.add(cheese01)
meat01 = Item(order=order01, name="Meat", cost=1.10,
              description="meat")
session.add(meat01)

# Commit data to database
session.commit()

print("Sample data added...")
