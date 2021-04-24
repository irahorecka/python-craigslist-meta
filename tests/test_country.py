import pytest
from fixtures import get_keys, get_children, get_title
from craigslist_meta import Country

selector = "country"
key = "germany"


def test_keys(get_keys):
    """Test `keys` method for country returns valid keys for instantiation."""
    country_keys = Country.keys
    expected_keys = sorted(list(set(get_keys(selector))))
    assert country_keys == expected_keys


def test_key():
    """Test `key` attribute of country instance."""
    country_key = Country(key).key
    expected_key = key
    assert country_key == expected_key


def test_children(get_children):
    """Test `children` attribute of country instance."""
    country_children = Country(key).children
    expected_children = list(get_children(selector, key))
    assert country_children == expected_children


def test_title(get_title):
    """Test `title` attribute of country instance."""
    country_title = Country(key).title
    expected_title = get_title(selector, key)
    assert country_title == expected_title


def test_url_raises():
    """`url` attribute should raise an exception for Country."""
    with pytest.raises(AttributeError, match="'Country' object has no attribute 'url'"):
        Country(key).url


def test_all():
    """Test `all` method yields all country instances."""
    country_instances = [country for country in Country.all()]
    assert all(isinstance(item, Country) for item in country_instances)


def test_key_raises():
    """Constructing Country with an invalid key should raise an exception."""
    with pytest.raises(ValueError):
        Country("invalid_key")
