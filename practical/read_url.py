import urllib

url = "http://media.pragprog.com/titles/gwpy/code/fileproc/hopedale.txt"

web_page = urllib.urlopen(url)
for line in web_page:
    line = line.strip()
    print line
web_page.close()
