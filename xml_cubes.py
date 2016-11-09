import xml.etree.ElementTree as ET

tree = ET.fromstring(input())

p = {'red':0, 'green':0, 'blue':0}
def add_points(tree, level):
    color = tree.attrib['color']
    p[color] = p.get(color, 0) + level
    for el in tree.findall('./cube'):
        add_points(el, level + 1)


add_points(tree, 1)

print(str(p['red']) + " " + str(p['green']) + " " + str(p['blue']))