import pytest
from fixtures import get_title, get_url
from craigslist_meta import Site

selector = "area"
# use a site key with areas
site_key = "sfbay"


@pytest.fixture
def area():
    """ Get an instance of Area. """
    area = next(iter(Site(site_key)))
    global area_key
    area_key = area.key
    yield area


def test_key(area):
    """ Test `key` attribute of area instance. """
    expected_key = area._key
    assert area_key == expected_key


def test_title(area, get_title):
    """ Test `title` attribute of area instance. """
    area_title = area.title
    expected_title = get_title(selector, area_key)
    assert area_title == expected_title


def test_url(area, get_url):
    """ Test `url` attribute of area instance. """
    area_url = area.url
    expected_url = get_url(selector, area_key)
    assert area_url == expected_url


def test_all_raises(area):
    """ `all` class method should raise an exception for Area. """
    with pytest.raises(AttributeError, match="'Area' object has no attribute 'all'"):
        area.all()


def test_keys_raises(area):
    """ `keys` class method should raise an exception for Area. """
    with pytest.raises(AttributeError, match="'Area' object has no attribute 'keys'"):
        area.keys()


def test_children_raises(area):
    """ `children` attribute should raise an exception for Area. """
    with pytest.raises(AttributeError, match="'Area' object has no attribute 'children'"):
        area.children
