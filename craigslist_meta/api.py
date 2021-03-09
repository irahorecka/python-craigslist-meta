from .base import Base


class Area(Base):
    """ Parse Craigslist areas. """

    _selector_key = "area"

    def __init__(self, key):
        self._key = key

    @staticmethod
    def __iter__():
        # `Area` does not have a subclass
        yield from ()

    @staticmethod
    def all():
        """ Unlike `Region`, `Country`, and `Site`, `Area` does not
        have a subclass and therefore this method should be removed. """
        raise NotImplementedError("type object 'Area' has no attribute 'all'")


class Site(Base):
    """ Parse Craiglist sites. """

    _selector_key = "site"
    _subclass = Area

    def __init__(self, key):
        self._key = key

    def has_area(self):
        """ Boolean value for if site has areas. For example, `Site('sfbay')` has areas,
        `Site('monterey')` does not. """
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
        self._key = key

    @property
    def url(self):
        """ Unlike `Site` and `Area`, `Country` does not have a url -
        therefore, `Base.url()` should be silenced. """
        raise NotImplementedError("type object 'Country' has no attribute 'url'")


class Region(Base):
    """ Parse Craiglist regions. """

    _selector_key = "region"
    _subclass = Country

    def __init__(self, key):
        self._key = key

    @property
    def url(self):
        """ Unlike `Site` and `Area`, `Region` does not have a url -
        therefore, `Base.url()` should be silenced. """
        raise NotImplementedError("type object 'Region' has no attribute 'url'")
