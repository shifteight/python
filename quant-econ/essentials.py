def p(x, coeff):
	return sum([a * (x ** i) for i, a in enumerate(coeff)])

def count_capitals(s):
	us = s.upper()
	count = 0
	for i in range(len(s)):
		if s[i].isalpha() and us[i] == s[i]:
			count += 1
	return count

def is_subset(seq_a, seq_b):
	for a in seq_a:
		if not a in seq_b:
			return False
	return True