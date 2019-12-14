import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


def scrape_comic(url):
    resp = urllib.request.urlopen(url)
    html = resp.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    comic = soup.find(class_="comicpane")
    image = comic.find('img')
    title = soup.find(class_='post-title').find('a')
    previous = soup.find('a', class_='navi-prev')['href']
    nxt = soup.find('a', class_='navi-next')
    if nxt:
        nxt = nxt['href']
    return image['src'], image['alt'], title.string, previous, nxt
