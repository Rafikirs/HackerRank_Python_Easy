# Exercise: HTML Parser - Part 1
# URL: https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
# Description: Parsing HTML code

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value if value else 'None'}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value if value else 'None'}")

N = int(input())
html_code = "".join(input() for _ in range(N))

parser = MyHTMLParser()
parser.feed(html_code)
