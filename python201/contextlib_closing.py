from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as webpage:
    for line in webpage:
        # process the line
        pass