__author__ = 'kevin'


class Range(object):
    """A class that minic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self, k):
        """A more efficient implementation of lookup than default support."""
        return self._start <= k < (self._start + self._length * self._step) \
            and k % (self._step - self._start) == 0


if __name__ == '__main__':

    r = Range(0, 2000000000, 100)
    print(100000001 in r)
    print(100000001 in r)
