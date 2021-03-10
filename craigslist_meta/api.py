from .base import Base
from .metadata import REGIONS, COUNTRIES, SITES


class Area(Base):
    """ Parse Craigslist areas. """

    _selector_key = "area"

    def __init__(self, key):
        super().__init__(key)

    def __iter__(self):
        # Area does not have a subclass
        yield from ()

    @staticmethod
    def all():
        """ Unlike Region, Country, and Site, Area does not
        have a subclass - therefore, Area.all() should be invalidated. """
        raise AttributeError("'Area' object has no attribute 'all'")


class Site(Base):
    """ Parse Craiglist sites. """

    _selector_key = "site"
    _subclass = Area

    def __init__(self, key):
        super().__init__(key)

    def has_area(self):
        """ Return true if site has areas. For example, Site('sfbay') has areas,
        Site('monterey') does not. """
        try:
            next(self.__iter__())
            return True
        except StopIteration:
            return False


class Country(Base):
    """ Parse Craiglist countries. """

    _selector_key = "country"
    _subclass = Site

    def __init__(self, key):
        super().__init__(key)

    @property
    def url(self):
        """ Unlike Site and Area, Country does not have a url -
        therefore, Country.url attribute should be invalidated. """
        raise AttributeError("'Country' object has no attribute 'url'")


class Region(Base):
    """ Parse Craiglist regions. """

    _selector_key = "region"
    _subclass = Country

    def __init__(self, key):
        super().__init__(key)

    @property
    def url(self):
        """ Unlike Site and Area, Region does not have a url -
        therefore, Region.url attribute should be invalidated. """
        raise AttributeError("'Region' object has no attribute 'url'")
