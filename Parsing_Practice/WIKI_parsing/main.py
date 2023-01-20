import requests
import lxml
from bs4 import BeautifulSoup
import certifi


# search = 'Аватар (франшиза)'
# url = "https://ru.wikipedia.org/wiki/"+search
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '
#                          'Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
#
#
# r = requests.get(url, headers=headers,verify=certifi.where())
# r_text = bytes(r.text,'utf8')
# print(r.text)
# print(type(r.text))
# with open("index.html",'wb') as file:
#     file.write(r_text)





with open("index.html",'rb') as file:
    src = file.read()

# print(src)
soup = BeautifulSoup(src,"lxml")
title = soup.title

soderjanie = soup.find("div", class_='')
print(soderjanie.hre)
