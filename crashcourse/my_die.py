from die import Die

print("Roll a 6-sides die 10 times:")
my_die = Die()
for i in range(10):
    my_die.roll_die()

print("Roll a 20-sides die 10 times:")
another_die = Die(20)
for i in range(10):
    another_die.roll_die()