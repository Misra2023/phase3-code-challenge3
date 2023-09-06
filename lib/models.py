from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine (SQLite in this example)
engine = create_engine('sqlite:///restaurant_reviews.db')
Base = declarative_base()

#  Define the Restaurant model
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define the relationship with Review
    reviews = relationship('Review', back_populates='restaurant')

# Define the Customer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
 # Define the relationship with Review
    reviews = relationship('Review', back_populates='customer')

    # Define the Review model
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define the relationships with Restaurant and Customer
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews'):