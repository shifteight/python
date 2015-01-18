import string

s = 'The quick brown fox jumped over the lazy dog.'
t = s.maketrans('abegiloprstz', '463611092572')


print(s)
print(s.translate(t))