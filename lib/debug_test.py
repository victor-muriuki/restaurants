from customers import Customer
from restaurants import Restaurant
from reviews import Review


def debugging_test():
    # Create customers
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Jane", "Smith")

    # Create restaurants
    restaurant1 = Restaurant("Pizza Place")
    restaurant2 = Restaurant("Burger Joint")

    # Add reviews
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer1, restaurant2, 5)
    review3 = Review(customer2, restaurant1, 3)

    # Test methods
    print("Customer Methods:")
    print("Customer Full Name:", customer1.full_name())
    print("Customer Reviewed Restaurants:", customer1.restaurants())

    print("\nRestaurant Methods:")
    print("Restaurant Name:", restaurant1.name())
    print("Restaurant Reviews:", restaurant1.reviews())
    print("Restaurant Average Rating:", restaurant1.average_star_rating())

    print("\nReview Methods:")
    print("Review Rating:", review1.rating())
    print("Review Customer:", review1.customer().full_name())
    print("Review Restaurant:", review1.restaurant().name())

    print("\nAggregate and Association Methods:")
    print("Number of Reviews by Customer:", customer1.num_reviews())
    print("Find Customer by Name:", Customer.find_by_name("John Doe").full_name())
    print("Find All Customers by Given Name:", [c.full_name() for c in Customer.find_all_by_given_name("John")])

if __name__ == "__main__":
    debugging_test()
