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

    @property
    def url(self):
        """ Return craigslist url of `Area` instance. """
        return self._search_tree("url")

    @staticmethod
    def all():
        """ Unlike `Continent`, `Country`, and `Site`, `Area` does not
        have a subclass and therefore this method should be removed. """
        raise NotImplementedError("type object 'Area' has no attribute 'all'")


class Site(Base):
    """ Parse Craiglist sites. """

    _selector_key = "site"
    _subclass_selector_key = "area"
    _subclass = Area

    def __init__(self, key):
        self._key = key

    @property
    def url(self):
        """ Return craigslist url of Site instance. """
        return self._search_tree("url")

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
    _subclass_selector_key = "site"
    _subclass = Site

    def __init__(self, key):
        self._key = key


class Continent(Base):
    """ Parse Craiglist continents. """

    _selector_key = "continent"
    _subclass_selector_key = "country"
    _subclass = Country

    def __init__(self, key):
        self._key = key
