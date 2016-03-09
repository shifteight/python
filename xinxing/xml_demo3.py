from xml.dom.minidom import *

x = parse("xin.xml")
nx = x.getElementsByTagName("author")
print(nx[0].getAttribute("birth"))
print(nx[0].childNodes[0].data)
