import pytest
from fixtures import get_keys, get_children, get_title
from craigslist_meta import Country

selector = "country"
key = "germany"


def test_keys_country(get_keys):
    """ Test every country key is valid. """
    country_keys = [country.key for country in Country.all()]
    expected_keys = list(get_keys(selector))
    assert country_keys == expected_keys


def test_children_country(get_children):
    """ Test children of country instance. """
    country_children = Country(key).children
    expected_children = list(get_children(selector, key))
    assert country_children == expected_children


def test_title_country(get_title):
    """ Test title of country instance. """
    country_title = Country(key).title
    expected_title = get_title(selector, key)
    assert country_title == expected_title


def test_url_raises():
    """ url attribute should raise an exception for Country. """
    with pytest.raises(AttributeError, match="'Country' object has no attribute 'url'"):
        Country(key).url


def test_all():
    """ Test output of Country.all() are all country instances. """
    country_instances = [country for country in Country.all()]
    assert all(isinstance(item, Country) for item in country_instances)


def test_key_raises():
    """ Constructing Country with an invalid key should raise an exception. """
    with pytest.raises(ValueError):
        Country("invalid_key")
