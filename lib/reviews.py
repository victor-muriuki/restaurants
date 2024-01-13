# reviews.py
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        restaurant.restaurant_reviews.append(self)
        customer.customer_reviews.append(self)

    def rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
