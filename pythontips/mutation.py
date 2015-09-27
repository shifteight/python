foo = ['hi']
# print(foo)

bar = foo
bar += ['bye']
# print(foo)

def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))  # [1]
print(add_to(2))  # [1, 2]
print(add_to(3))  # [1, 2, 3]

def add_to_fresh(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to_fresh(1))  # [1]
print(add_to_fresh(2))  # [2]
print(add_to_fresh(3))  # [3]