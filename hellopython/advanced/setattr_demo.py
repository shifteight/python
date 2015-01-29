class TestSetAttr(object):

    def __init__(self):
        self.__dict__['things'] = {}  # set up replacement dict
    
    def __setattr__(self, name, value):
        print "Setting '%s' to '%s'" % (name, value)
        self.things[name] = value

    def __getattr__(self, name):
        try:
            return self.things[name]
        except KeyError:
            raise AttributeError(
                "'%s' object has no attribute '%s'" %
                (self.__class__.__name__, name))


test_class = TestSetAttr()
test_class.something = 42
print test_class.something
print test_class.things
print test_class.something_else
