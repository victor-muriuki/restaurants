# customers.py
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customer_reviews = []
        Customer.all_customers.append(self)

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def reviewed_restaurants(self):
        return list(set([review.restaurant for review in self.customer_reviews]))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        return new_review

    def num_reviews(self):
        return len(self.customer_reviews)

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all_customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]
