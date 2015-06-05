def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n - 1)

def binomial_rv(n, p):
	""" Generate one draw of binomial distribution. """
	from random import uniform
	v = 0
	for i in range(n):
		if uniform(0, 1) < p:
			v += 1
	return v

def find_pi(size):
	""" Compute an approximation to PI using Monte Carlo. """
	from random import uniform
	from math import sqrt

	count = 0
	for i in range(size):
		x = uniform(0, 1)
		y = uniform(0, 1)
		if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) < 0.5:
			count += 1

	area = count * 1.0 / size
	return area / (0.5 * 0.5)

def pay_game():
	""" Get one realization of the following random device:
	* Flip an unbiased coin 10 times
	* If 3 consecutive heads occur one or more times within this sequence,
	  pay one dollar
	* If not, pay nothing
	"""
	from random import uniform

	payoff = 0
	count = 0

	for i in range(10):
		U = uniform(0, 1)
		count = count + 1 if U < 0.5 else 0
		if count == 3:
			payoff = 1

	return payoff

def generate_ts(T, alpha):
	""" Simulate the correlated time series
	    x(t+1) = alpha * x(t) + epsilon(t+1),
	    where x(0) = 0, t = 0, ..., T. {epsilon(t)} are iid standard normals.
	"""
	from random import normalvariate

	x = [0] * (T + 1)
	for i in range(T):
		x[i+1] = alpha * x[i] + normalvariate(0, 1)

	return x

# Plot the series
import matplotlib.pyplot as plt
plt.plot(generate_ts(200, 0.9), 'b-')

# Plot with legends
