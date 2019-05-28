from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['A', 'B', 'C']
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

ics = IceCreamStand("ICS_A", 'TYPE_A')
ics.show_flavors()