def fibqyx(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


"""
Pascal Triangle
"""


def triangles():
    n, line = 0, [1]
    while True:
        yield line
        line = [1] + [line[i] + line[i + 1]
                      for i in range(len(line) - 1)] + [1]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
