from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_desciptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("Upgrading...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()