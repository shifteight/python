# TODO: find bugs in this program!

def double_preceding(values):
    if values == []:
        pass
    else:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]

values = [1, 2, 3]
double_preceding(values)
print(values)   # [0, 2, 4]
