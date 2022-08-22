
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree
import codecs
import json

array=[]
f = open('test.json')
data = json.load(f)
for i in data:
    page_to_scrape = requests.get(codecs.decode('https://en.wikipedia.org/wiki/{}'.format(i), 'unicode-escape'))
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    txt=soup.find_all('h1',class_="firstHeading")
    s1=soup.find_all('a',rel="discussion")
    for link in s1 :
     if(link.get('title').find("exist")!=-1):
         array.append(txt[0].string)
     else: 
         array.append(txt[0].string+"   this page does not exist")
f.close()

f = open("writeToFile.txt", "w")
for word in array:
    f.write(word+'\n')
f.close()
