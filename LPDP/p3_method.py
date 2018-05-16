class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_person(self,):
        return "<Person (%s, %s)>" % (self.name, self.age)


p = Person("John", 32)
print("Type of object:", type(p), "Memory address:", id(p))