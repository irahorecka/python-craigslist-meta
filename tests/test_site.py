import pytest
from fixtures import get_keys, get_children, get_title, get_url
from craigslist_meta import Site

selector = "site"
key = "sfbay"


def test_keys(get_keys):
    """ Test every site key is valid. """
    site_keys = [site.key for site in Site.all()]
    expected_keys = list(get_keys(selector))
    assert site_keys == expected_keys


def test_children(get_children):
    """ Test `children` attribute of site instance. """
    site_children = Site(key).children
    expected_children = list(get_children(selector, key))
    assert site_children == expected_children


def test_title(get_title):
    """ Test `title` attribute of site instance. """
    site_title = Site(key).title
    expected_title = get_title(selector, key)
    assert site_title == expected_title


def test_url(get_url):
    """ Test `url` attribute of site instance. """
    site_url = Site(key).url
    expected_url = get_url(selector, key)
    assert site_url == expected_url


def test_has_area():
    """ Test `has_area` method of a site instance. """
    has_area = Site("boston").has_area()
    expected_has_area = True
    assert has_area == expected_has_area

    has_area = Site("eugene").has_area()
    expected_has_area = False
    assert has_area == expected_has_area


def test_all():
    """ Test `all` method yields all site instances. """
    site_instances = [site for site in Site.all()]
    assert all(isinstance(item, Site) for item in site_instances)


def test_key_raises():
    """ Constructing Site with an invalid key should raise an exception. """
    with pytest.raises(ValueError):
        Site("invalid_key")
