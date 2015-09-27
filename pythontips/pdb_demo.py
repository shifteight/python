# Run pdb from inside a script

import pdb

def make_bread():
	pdb.set_trace()
	return "I don't have time"

print(make_bread())