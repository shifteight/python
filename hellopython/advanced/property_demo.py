class TestProperty(object):

    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        if not (type(value) == int and 0 <= value < 32):
            raise ValueError("TestProperty.x must be an int from 0 to 31")
        self._x = value

    x = property(get_x, set_x)


test = TestProperty(10)
print test.x
test.x = 11
test.x += 1
assert test.x == 12
print test.x

try:
    test2 = TestProperty(42)
except ValueError:
    print "test2 not set to 42"
