

class Reviews:

    review_list= []
    def __init__(self, customer, restaurant, rating):
        self._customer_obj = customer
        self._restaurant_obj = restaurant
        self.rating = rating

    def rating (self):
        return self.rating

    
    @classmethod
    def all(cls):
        return  cls.review_list   
    

    def customer(self):
        return self._customer_obj
    
    def restaurant(self):
        return self._restaurant_obj 
   
    