def narcissistic_number_1(num):
    length = len(str(num))
    count = length
    num_sum = 0
    while count:
        num_sum += ((num // 10 ** (count - 1)) % 10) ** length
        count -= 1
    else:
        return num_sum == num


for i in range(10**6):
    if narcissistic_number_1(i):
        print("%d is %d bit narcissistic_number" % (i, len(str(i))))
