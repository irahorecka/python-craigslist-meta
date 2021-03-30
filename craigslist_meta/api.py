from .base import Base, classproperty


class Area(Base):
    """ Parse Craigslist areas. """

    _selector_key = "area"

    def __init__(self, key):
        self._key = key

    def __iter__(self):
        # Area does not have a subclass
        yield from ()

    @classproperty
    def all(cls):
        """ Area does not have a subclass - Area.get_all() should be invalidated. """
        raise AttributeError("'Area' object has no attribute 'all'")

    @classproperty
    def keys(cls):
        """ Area is not a public class - Area.get_keys() should be invalidated. """
        raise AttributeError("'Area' object has no attribute 'keys'")

    @property
    def children(self):
        """ Area has no children. """
        raise AttributeError("'Area' object has no attribute 'children'")


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
        """ Country does not have a url. """
        raise AttributeError("'Country' object has no attribute 'url'")


class Region(Base):
    """ Parse Craiglist regions. """

    _selector_key = "region"
    _subclass = Country

    def __init__(self, key):
        super().__init__(key)

    @property
    def url(self):
        """ Region does not have a url. """
        raise AttributeError("'Region' object has no attribute 'url'")
