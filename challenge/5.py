import urllib, pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

lines = urllib.urlopen(url).readlines()
data = pickle.loads(''.join(lines))

for row in data:
    result = ''
    for chars in row:
        result += chars[0] * chars[1]
    print result
