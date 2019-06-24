__author__ = 'kevin'

import string

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', err)

print('safe_substitute():', t.safe_substitute(values))

