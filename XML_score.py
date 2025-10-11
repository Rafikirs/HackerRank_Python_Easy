# Exercise: XML 1 - Find the Score
# URL: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
# Description: Find the score of a given XML document

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)
    
    for child in node:
        score += get_attr_number(child)
    
    return score


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
