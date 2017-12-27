from collections import defaultdict


# example 1:
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d1 = defaultdict(int)
for word in words:
    d1[word] += 1

print(d1)


# example 2:
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.56), (678, 300.25), (1234, 35.67)]

d2 = defaultdict(list)
for acct_num, value in my_list:
    d2[acct_num].append(value)

print(d2)

# example 3:

animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print(animal)
print(animal['Nick'])