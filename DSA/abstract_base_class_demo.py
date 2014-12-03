from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the seq; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def __eq__(self, other):
        """Return True if the two sequences are element by element equivalent."""
        if len(self) != len(other):
            return False
        else:
            for j in range(len(self)):
                if self[j] != other[j]:
                    return False
        return True
    
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
