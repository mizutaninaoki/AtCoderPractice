import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    count = 0
    for child in node.iter():
        # print(child)
        # print(child.attrib)
        count += len(child.attrib)
    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# get_attr_numberのコメントされているprint()を有効にしたときに返ってくる値
# <Element 'feed' at 0x23996e0 >
# {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
# <Element 'title' at 0x2399718>
# {}
# <Element 'subtitle' at 0x2399750>
# {'lang': 'en'}
# <Element 'link' at 0x2399788>
# {'rel': 'alternate', 'type': 'text/html', 'href': 'http://hackerrank.com/'}
# <Element 'updated' at 0x23997c0>
# {}
