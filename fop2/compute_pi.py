"""
Computes PI using Gottfried Leibniz's method.
Allows to specify iterations.
"""


def compute_pi(iterations):
    sum = 0

    for i in range(iterations):
        sum += (-1)**(i) / (2 * i + 1)

    return 4 * sum


def main():
    iterations = int(input("Enter the number of iteration:"))
    pi = compute_pi(iterations)
    print("PI =", pi, "(with", iterations, "iterations)")


if __name__ == '__main__':
    main()
