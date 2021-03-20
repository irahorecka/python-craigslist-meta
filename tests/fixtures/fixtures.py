""" Common pytest fixtures. """

import pytest
from craigslist_meta import base, metadata


@pytest.fixture
def get_keys():
    """ Get all keys of a given class. """
    yield lambda selector: base.find_keys(metadata.CRAIGSLIST, selector)


@pytest.fixture
def get_children():
    """ Get children of a given instance. """
    yield lambda selector, key: base.find_children(metadata.CRAIGSLIST, selector, key)


@pytest.fixture
def get_title():
    """ Get title of a given instance. """
    yield lambda selector, key: base.find_title(metadata.CRAIGSLIST, selector, key)


@pytest.fixture
def get_url():
    """ Get url of a given instance. """
    yield lambda selector, key: base.find_url(metadata.CRAIGSLIST, selector, key)
