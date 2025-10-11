# Exercise: HTML Parser - Part 2
# URL: https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true
# Description: Parsing HTML code

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            for line in data.splitlines():
                print(line)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data.strip(): 
            print(">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += input() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
