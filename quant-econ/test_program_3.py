from random import uniform
import matplotlib.pyplot as plt

def generate_data(n, generator_type):
	return [generator_type(0, 1) for i in range(n)]

data = generate_data(100, uniform)
plt.plot(data, 'b-')
plt.show()