class ReversedSequenceIterator:
    """A reversed iterator for any of Python's sequence types."""

    def __init__(self, sequence):

        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):

        self._k -= 1
        if self._k >= 0:
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self

if __name__ == '__main__':

    rsi = ReversedSequenceIterator([1,2,3])
    print(next(rsi))
    print(next(rsi))
    print(next(rsi))
    print(next(rsi))
    
