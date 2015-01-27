import urllib2
from BeautifulSoup import BeautifulSoup

def get_stock_html(ticker_name):

    # create opener object
    opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
    )

    # add headers to request; pretending to be IE7 on Windows XP
    opener.addheaders = [
        ('User-agent',
         "Mozilla/4.0 (compatible; MSIE 7.0; "
         "Windows NT 5.1; .NET CLR 2.0.50727; "
         ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]

    # read page with opener
    url = "http://finance.yahoo.com/q?s=" + ticker_name
    response = opener.open(url)
    return ''.join(response.readlines())


def find_quote_section(html):

    # create parse object
    soup = BeautifulSoup(html)

    # find yfi_quote_summary element
    quote = soup.find('div',
                      attrs={'class': 'yfi_quote_summary'})
    return quote

if __name__ == '__main__':
    html = get_stock_html('GOOG')
    print find_quote_section(html)
