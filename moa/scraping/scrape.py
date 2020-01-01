import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def _short(url):
    path = urlparse(url).path
    if path.startswith('/'):
        path = path[1:]
    if path.endswith('/'):
        path = path[:-1]
    return path


def _image_date(image_src):
    name = image_src.split('/')[-1]
    return name[:10]


def scrape_comic(url):
    resp = urllib.request.urlopen(url)
    html = resp.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    comic = soup.find(class_="comicpane")
    image = comic.find('img')
    title = soup.find(class_='post-title').find('a')
    previous = _short(soup.find('a', class_='navi-prev')['href'])
    nxt = soup.find('a', class_='navi-next')
    if nxt:
        nxt = _short(nxt['href'])
    return image['src'], image['alt'], title.string, _image_date(image['src']), _short(title['href']), previous, nxt
