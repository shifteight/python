# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return None, None

    min = max = L[0]
    for x in L[1:]:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max


if __name__ == '__main__':
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
