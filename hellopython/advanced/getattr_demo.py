class TestGetAttr(object):

    def __getattr__(self, name):
        print "Attribute '%s' not found!" % name
        return 42

test_class = TestGetAttr()
print test_class.something

test_class.something = 43
print test_class.something
