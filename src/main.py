from bs4 import BeautifulSoup
import requests


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
    print(getTexts(next_link))
