__author__ = 'kevin'

import collections


class Vector(object):
    """Represent a vector in a multidimensional space."""

    def __init__(self, x):
        """Create an instance of Vector.

        If x is an integer, it produces an x-dim vector with all zeros;
        If x is an iterable sequence, it produces a vector with dimension
        equal to the length of that sequence and coordinates equal to the
        sequence values.
        """
        if isinstance(x, int):
            self._corrds = [0] * x
        if isinstance(x, collections.Sequence):
            self._corrds = x

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._corrds)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._corrds[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._corrds[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Return difference between two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, other):
        """Return the dot product of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = 0
        for j in range(len(self)):
            result += self[j] * other[j]
        return result

    # def __mul__(self, times):
    #     """Return a multiple of a vector. Support for syntax like `v * 3`."""
    #     if not isinstance(times, (int, float)):
    #         raise TypeError('multiple must be numeric')
    #     result = Vector(len(self))
    #     for j in range(len(self)):
    #         result[j] = self[j] * times
    #     return result
    #
    # def __rmul__(self, times):
    #     """Provide support for syntax like `3 * v`."""
    #     if not isinstance(times, (int, float)):
    #         raise TypeError('multiple must be numeric')
    #     return self.__mul__(times)

    def __neg__(self):
        """Return negation of a vector."""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinate as other."""
        return self._corrds == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._corrds)[1:-1] + '>'


if __name__ == '__main__':
    v = Vector(5)
    v[1] = 2
    v[-1] = 4
    print("v = ", v)
    u = v + v
    print("u = ", u)
    print("u * v = ", u * v)

    v1 = Vector([1, 2, 3])
    print(v1)