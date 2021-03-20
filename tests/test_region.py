import pytest
from fixtures import get_keys, get_children, get_title
from craigslist_meta import Region

selector = "region"
key = "asia"


def test_keys(get_keys):
    """ Test `keys` method for region returns valid keys for instantiation. """
    region_keys = Region.keys()
    expected_keys = sorted(list(set(get_keys(selector))))
    assert region_keys == expected_keys


def test_key():
    """ Test `key` attribute of region instance. """
    region_key = Region(key).key
    expected_key = key
    assert region_key == expected_key


def test_children(get_children):
    """ Test `children` attribute of region instance. """
    region_children = Region(key).children
    expected_children = list(get_children(selector, key))
    assert region_children == expected_children


def test_title(get_title):
    """ Test `title` attribute of region instance. """
    region_title = Region(key).title
    expected_title = get_title(selector, key)
    assert region_title == expected_title


def test_url_raises():
    """ `url` attribute should raise an exception for Region. """
    with pytest.raises(AttributeError, match="'Region' object has no attribute 'url'"):
        Region(key).url


def test_all():
    """ Test `all` method yields all region instances. """
    region_instances = [region for region in Region.all()]
    assert all(isinstance(item, Region) for item in region_instances)


def test_key_raises():
    """ Constructing Region with an invalid key should raise an exception. """
    with pytest.raises(ValueError):
        Region("invalid_key")
