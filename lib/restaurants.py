# restaurants.py
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.restaurant_reviews = []
        Restaurant.all_restaurants.append(self)

    def reviews(self):
        return self.restaurant_reviews

    def customers(self):
        return list(set([review.customer for review in self.restaurant_reviews]))

    def average_star_rating(self):
        reviews = self.reviews()
        if not reviews:
            return 0
        total_rating = sum(review.rating for review in reviews)
        return total_rating / len(reviews) if len(reviews) > 0 else 0
