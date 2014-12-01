# word frequency
# input: a list of words, seperated by whitespace
# output: appearing times of each word

d = {}

words = input("Enter a list of words, seperated by whitespace: ")

word_list = words.split()

for word in word_list:
    d[word] = d.get(word, 0) + 1

print(d.items())
