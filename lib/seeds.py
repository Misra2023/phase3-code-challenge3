# Add sample data (You can replace this with your own data)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review


engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadate.create_all(engine)
session = sessionmaker(bind=engine)
session = session()


customer1 = Customer(first_name='Misra', last_name='Abdi')
customer2 = Customer(first_name='yasmin', last_name='Hassan')
restaurant1 = Restaurant(name='Restaurant A', price=4)
restaurant2 = Restaurant(name='Restaurant B', price=5)
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

session.add_all([customer1, customer2, restaurant1, restaurant2, review1, review2])
session.commit()

