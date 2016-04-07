import urllib2, re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"

def do_nothing(nothing):
	while True:
		content = urllib2.urlopen(url+nothing).read()
		print content
		r = re.search('nothing is (\d+)', content)
		if r is None:
			break
		else:
			nothing = r.group(1)

# do_nothing(nothing)
