import xml.etree.ElementTree as et

x = et.Element("author")
x.text = "xinguimeng"
x.set("boy", "true")
b = et.SubElement(x, "birthday")
y = et.SubElement(b, "year")
y.text = "1992"
sx = et.tostring(x)
print(sx)
