class Doubler:
    """
    An infinite iterator
    """

    def __init__(self):
        """"""
        self.number = 0

    def __iter__(self):
        """"""
        return self

    def __next__(self):
        """"""
        self.number += 1
        return self.number * self.number


if __name__ == '__main__':
    doubler = Doubler()
    count = 0

    for number in doubler:
        print(number)
        if count > 5:
            break
        count += 1
