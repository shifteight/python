from xml.sax import *

class XinHandler(ContentHandler):
    def startDocument(self):
        print("---parsing begins---")
    def endDocument(self):
        print("---parsing ends---")
    def startElement(self, name, attrs):
        if name == "author":
            print("Name:", attrs['name'], "Date:", attrs['birth'])

parse("xin.xml", XinHandler())
