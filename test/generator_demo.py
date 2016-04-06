def double_numbers(iterable):
    for i in iterable:
        yield i + i

xrange_ = xrange(1, 900000000)

for i in double_numbers(xrange_):
    print i
    if i >= 30:
        break
