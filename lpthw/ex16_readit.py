from sys import argv

script, filename = argv

print "Opening file %r for read..." % filename

txt = open(filename)
print txt.read()

txt.close()
