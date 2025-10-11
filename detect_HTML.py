# Exercise: Detect HTML Tags, Attributes and Attribute Values
# URL: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
# Description: Detecting HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

# Lecture du HTML
html = ""
for _ in range(int(input())):
    html += input().strip() + "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()
