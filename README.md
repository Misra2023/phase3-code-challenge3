# phase3-code-challenge3
Restaurant Review Database
The Restaurant Review Database is a simple application that allows users to review and manage their favorite restaurants. This project is built using SQLAlchemy and Python.

Table of Contents
Prerequisites
Installation
Usage
Database Structure
Sample Data
Contributing
License
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.6 or higher installed on your machine.

SQLAlchemy library installed. You can install it using pip:

shell
Copy code
pip install sqlalchemy
Installation
Clone this repository to your local machine:

shell
Copy code
git clone https://github.com/your-username/restaurant-review-db.git
Navigate to the project directory:

shell
Copy code
cd restaurant-review-db
Create a virtual environment (optional but recommended):

shell
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

shell
Copy code
venv\Scripts\activate
On macOS and Linux:

shell
Copy code
source venv/bin/activate
Install the project dependencies:

shell
Copy code
pip inst

# Import the RestaurantReviewer class
from restaurant_reviewer import RestaurantReviewer

# Create an instance of RestaurantReviewer with a customer ID
reviewer = RestaurantReviewer(customer_id=1)

# Add reviews
print(reviewer.add_review("Restaurant A", 4.5))
print(reviewer.add_review("Restaurant B", 3.0))

# Find your favorite restaurant
print(reviewer.favorite_restaurant())

# Delete reviews
print(reviewer.delete_reviews("Restaurant B"))
Database Structure
The database has three main tables:

restaurants: Stores information about restaurants, including id, name, and price.

customers: Contains customer details such as id, first_name, and last_name.

reviews: Holds reviews with attributes like id, star_rating, restaurant_id, and customer_id. It establishes relationships between customers, restaurants, and reviews.


shell
Copy code
python add_sample_data.py
Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:

License
This project is licensed under the MIT License - see the LICENSE file for details.


