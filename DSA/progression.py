import math


class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current  # record current value to return
            self._advance()  # advance to prepare for next time
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print('  '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        increment  the fixed constant to add to each term (default 1)
        start   the first term of the progression (default 0)
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.

        base    the fixed constant multiplied to each term (default 2)
        start   the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.

        first    the first term (default 0)
        second   the second term (default 1)
        """
        super().__init__(first)
        self._prev = second - first  # fictitious value preceding the first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


class PairDiffProgression(Progression):
    """Iterator producing a progression in which each value is the
    absolute value of the difference between the previous two values.

    Constraint: the first two value must be positive!
    """

    def __init__(self, first=2, second=200):
        if first < 0 or second < 0:
            raise ValueError('first two values must be positive')
        super().__init__(first)
        self._prev = second + first

    def _advance(self):
        tmp = self._prev
        self._prev = self._current
        self._current = abs(tmp - self._current)


class ConsecutiveSqrtProgression(Progression):
    """Iterator producing a consecutive sqrt progression."""

    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        self._current = math.sqrt(self._current)

# testing for progressions
if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(10)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)

    print('PairDiff progression with default start values:')
    PairDiffProgression().print_progression(10)

    print('PairDiff progression with start values 3 and 5:')
    PairDiffProgression(3, 5).print_progression(10)

    print('Consecutive progression with default start values:')
    ConsecutiveSqrtProgression().print_progression(10)

    print('Consecutive progression with start value 10000:')
    ConsecutiveSqrtProgression(10000).print_progression(10)


