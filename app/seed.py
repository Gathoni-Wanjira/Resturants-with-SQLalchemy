#/home/gathoni/.pyenv/shims python 

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant,Customer, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///hospitality.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    fake = Faker()


    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
            name = fake.name_nonbinary(),
            price = random.randint(1500,3500)
            
        )

        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)
        
        
        customers = []
    for i in range(50):
        customer = Customer(
            first_name = fake.first_name(),
            last_name = fake.last_name()
        )

        # add and commit individually to get IDs back
        session.add(customer)
        session.commit()

        customers.append(customer)
        
        

    reviews = []
    for customer in customers:
        for i in range(random.randint(1,2)):
            restaurant = random.choice(restaurant)
            
            
            review = Review(
                star_ratings=random.randint(0, 10),
                restaurant_id =fake.sentence(),
                customer_id=review.id,
            )
            session.add(review)
            session.commit()
            reviews.append(review)
            
    session.close()
