import pytest
from fixtures import get_title, get_url
from craigslist_meta import Site

selector = "area"
# use a area key with areas
site_key = "sfbay"


@pytest.fixture
def area():
    """ Get an instance of Area. """
    area = next(iter(Site(site_key)))
    global area_key
    area_key = area.key
    yield next(iter(Site(site_key)))


def test_children_raises(area):
    """ children attribute should raise an exception for Area. """
    with pytest.raises(AttributeError, match="'Area' object has no attribute 'children'"):
        area.children


def test_title_site(area, get_title):
    """ Test title of area instance. """
    site_title = area.title
    expected_title = get_title(selector, area_key)
    assert site_title == expected_title


def test_url(area, get_url):
    """ Test url of area instance. """
    site_url = area.url
    expected_url = get_url(selector, area_key)
    assert site_url == expected_url


def test_all_raises(area):
    """ all class attribute should raise an exception for Area. """
    with pytest.raises(AttributeError, match="'Area' object has no attribute 'all'"):
        area.all()
