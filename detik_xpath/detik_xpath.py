import urllib2
from bs4 import BeautifulSoup

class DetikXpath:
    @classmethod
    def parsing_html(self, url):
        result_tag = urllib2.urlopen(url)
        parsing = BeautifulSoup(result_tag.read(), "html.parser")
        result_parsing = parsing.findAll("img")
        return result_parsing
