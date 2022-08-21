from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree
import numpy
import codecs
import json

array=[]
f = open('test.json')
data = json.load(f)
for i in data:
    page_to_scrape = requests.get(codecs.decode('https://en.wikipedia.org/wiki/{}'.format(i), 'unicode-escape'))
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    txt=soup.find_all('h1',class_="firstHeading")
    print(txt[0].string)
    array.append(txt[0].string)
f.close()


f = open("writeToFile.txt", "w")
for word in array:
    f.write(word+'\n')
f.close()