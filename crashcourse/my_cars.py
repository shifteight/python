from car import Car
from electric_car import Battery, ElectricCar

my_beetle = Car("wolkswagen", 'beetle', 2016)
print(my_beetle.get_desciptive_name())

my_tesla = ElectricCar("tesla", 'roadster', 2016)
print(my_tesla.get_desciptive_name())
my_tesla.battery.get_range()