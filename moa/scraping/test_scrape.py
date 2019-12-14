import os
import urllib

import pytest

from .scrape import scrape_comic


@pytest.fixture
def old():
    path = os.path.join(os.path.dirname(__file__), 'old.html')
    f = open(path, 'rb')
    yield f
    f.close()


@pytest.fixture
def new():
    path = os.path.join(os.path.dirname(__file__), 'new.html')
    f = open(path, 'rb')
    yield f
    f.close()


@pytest.fixture
def mock_old(monkeypatch, old):
    monkeypatch.setattr(urllib.request, 'urlopen', lambda url: old)


@pytest.fixture
def mock_new(monkeypatch, new):
    monkeypatch.setattr(urllib.request, 'urlopen', lambda url: new)


def test_scrape_comic_old(mock_old):
    image, alt, title, prev, nxt = scrape_comic('test')
    assert image == 'http://www.dumbingofage.com/comics/2019-12-13-wish.png'
    assert alt == 'END OF STORYLINE sorta'
    assert title == 'Wish'
    assert prev == 'http://www.dumbingofage.com/2019/comic/book-10/01-birthday-pursuit/5footturkey/'
    assert nxt == 'http://www.dumbingofage.com/2019/comic/book-10/02-to-remind-you-of-my-love/sixflags/'


def test_scrape_comic_new(mock_new):
    image, alt, title, prev, nxt = scrape_comic('test')
    assert image == 'http://www.dumbingofage.com/comics/2019-12-14-sixflags.png'
    assert alt == 'new storyline means new flashback now, apparently'
    assert title == 'Six Flags'
    assert prev == 'http://www.dumbingofage.com/2019/comic/book-10/01-birthday-pursuit/wish-2/'
    assert nxt is None
