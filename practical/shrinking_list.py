
def remove_neg(num_list):
    '''
    Remove the negative numbers from the list num_list.
    '''

    i = 0
    while i < len(num_list):
        if num_list[i] < 0:
            num_list.pop(i)
        else:
            i += 1

numbers = [1, 2, 3, -3, 6, -1, -3, 1]
remove_neg(numbers)
print(numbers)
