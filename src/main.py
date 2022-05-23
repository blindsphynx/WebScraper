from bs4 import BeautifulSoup
import requests
import re

def getLinksFromTable(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', border=1)
    links = []
    for a in table.find_all('a', href=True):
        links.append(a['href'])
    return links


def getTexts(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', cellpadding=10)
    return table.get_text()


URL = "http://rosvuz.dissernet.org/cases/148217"
array = getLinksFromTable(URL)

for i in range(len(array)):
    next_link = array[i]
    texts = re.split(r'(\[.+\s\d+\])', getTexts(next_link))

    file = open(F"текст{i}.txt", "w+", encoding='utf-8')
    file.write(texts[2])
    file.close()

    file = open(F"плагиат{i}.txt", "w+", encoding='utf-8')
    file.write(texts[4])
    file.close()
