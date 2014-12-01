__author__ = 'kevin'


class Vector(object):
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dim vector of zeros."""
        self._corrds = [0] * d

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
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v:
        total += entry