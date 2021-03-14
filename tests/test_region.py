import pytest
from fixtures import get_keys, get_children, get_title
from craigslist_meta import Region

selector = "region"
key = "asia"


def test_keys_region(get_keys):
    """ Test every region key is valid. """
    region_keys = [region.key for region in Region.all()]
    expected_keys = list(get_keys(selector))
    assert region_keys == expected_keys


def test_children_region(get_children):
    """ Test children of region instance. """
    region_children = Region(key).children
    expected_children = list(get_children(selector, key))
    assert region_children == expected_children


def test_title_region(get_title):
    """ Test title of region instance. """
    region_title = Region(key).title
    expected_title = get_title(selector, key)
    assert region_title == expected_title


def test_url_raises():
    """ url attribute should raise an exception for Region. """
    with pytest.raises(AttributeError, match="'Region' object has no attribute 'url'"):
        Region(key).url


def test_all():
    """ Test output of Region.all() are all region instances. """
    region_instances = [region for region in Region.all()]
    assert all(isinstance(item, Region) for item in region_instances)


def test_key_raises():
    """ Constructing Region with an invalid key should raise an exception. """
    with pytest.raises(ValueError):
        Region("invalid_key")
