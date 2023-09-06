# Create a session to interact with the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create a SQLAlchemy database engine (SQLite in this example)
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

def full_name(self):
        return f"{self.first_name} {self.last_name}"

class RestaurantReviewer:
    def __init__(self):
        self.reviews = {}

    def favorite_restaurant(self):
        if not self.reviews:
            return "You haven't reviewed any restaurants yet."
        
        favorite = max(self.reviews, key=self.reviews.get)
        return f"Your favorite restaurant is '{favorite}' with a rating of {self.reviews[favorite]}."

    def add_review(self, restaurant, rating):
        if rating < 1 or rating > 5:
            return "Rating must be between 1 and 5."

        self.reviews[restaurant] = rating
        return f"Review added for '{restaurant}' with a rating of {rating}."

    def delete_reviews(self, restaurant):
        if restaurant in self.reviews:
            del self.reviews[restaurant]
            return f"Reviews for '{restaurant}' have been deleted."
        else:
            return f"You haven't reviewed '{restaurant}'."

# Example usage:
reviewer = RestaurantReviewer()

print(reviewer.add_review("Restaurant A", 4.5))
print(reviewer.add_review("Restaurant B", 3.0))
print(reviewer.add_review("Restaurant C", 4.8))

print(reviewer.favorite_restaurant())

print(reviewer.delete_reviews("Restaurant B"))
print(reviewer.favorite_restaurant())
