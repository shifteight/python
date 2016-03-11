from xml.dom.minidom import *

def scannode(doc, level=0):
    ret = doc.__class__.__name__
    if doc.nodeType == Node.ELEMENT_NODE:
        ret += ", tag:" + doc.tagName
    print(" " * level * 4, ret)
    if doc.hasChildNodes:
        for child in doc.childNodes:
            scannode(child, level+1)

x = parse("book.xml")
print(x)
scannode(x)
