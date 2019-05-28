class Restaurant():

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    
    def describle_restaurant(self):
        description = self.restaurant_name + ' ' + self.cuisine_type
        print(description.title())
    
    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, increment):
        self.number_served += increment
    
if __name__ == '__main__':
    r_A = Restaurant("Rest_A", 'Type_A')
    r_A.describle_restaurant()
    r_A.open_restaurant()

