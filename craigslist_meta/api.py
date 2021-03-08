from .metadata import CRAIGSLIST


class Base:
    """ Base class for Continent, Country, Site, and Area. """

    def __init__(self):
        self._key_selector = ""
        self._key = ""
        self._subclass_key = ""
        self._subclass = None

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self._key)

    def __len__(self):
        return len(self._unique_subclass_keys())

    def __iter__(self):
        """ Yield unique instance(s) of caller's subclass if it exists.
        Sublass instances are within scope of the caller's instance; for example,
        `Continent('africa')` will yield all unique `Country` instances that are in Africa. """
        yield from (self._subclass(subclass_key) for subclass_key in self._unique_subclass_keys())

    def _unique_subclass_keys(self):
        """ Return a list of unique keys within scope of the caller's instance.
        For example, `Continent('africa')` will return ['egypt', 'ethiopia', 'ghana', ...] """
        return list(
            {
                region[self._subclass_key]["key"]
                for region in self._filter_tree()
                if region.get(self._subclass_key)
            }
        )

    def _filter_tree(self):
        """ Yield a sequence of dictionaries that fulfill the
        instance's filter as determined by its key. """
        yield from filter(
            lambda leaf: leaf.get(self._key_selector)
            and leaf[self._key_selector]["key"] == self._key
            if self._key
            else leaf[self._key_selector]["key"],
            CRAIGSLIST,
        )

    @property
    def key(self):
        """ Return key of the instance. """
        return self._key

    @property
    def title(self):
        """ Return title of the instance. """
        return self._search_tree("title")

    @property
    def url(self):
        """ Return url of the instance if it exists. """
        return self._search_tree("url")

    def _search_tree(self, key):
        """ Return value for `key` within the instance's filtered values. """
        try:
            return next(self._filter_tree())[self._key_selector].get(key)
        except StopIteration:
            return None


class Continent(Base):
    """ Parse Craiglist continents. """

    def __init__(self, key=""):
        self._key_selector = "continent"
        self._key = key
        self._subclass_key = "country"
        self._subclass = Country


class Country(Base):
    """ Parse Craiglist countries. """

    def __init__(self, key=""):
        self._key_selector = "country"
        self._key = key
        self._subclass_key = "site"
        self._subclass = Site


class Site(Base):
    """ Parse Craiglist sites. """

    def __init__(self, key=""):
        self._key_selector = "site"
        self._key = key
        self._subclass_key = "area"
        self._subclass = Area

    def has_area(self):
        """ Boolean value for if site has areas. For example, `Site('sfbay')` has areas,
        `Site('monterey')` does not. """
        try:
            next(self.__iter__())
            return True
        except StopIteration:
            return False


class Area(Base):
    """ Parse Craigslist areas. """

    def __init__(self, key):
        self._key_selector = "area"
        self._key = key

    @staticmethod
    def __iter__():
        yield from ()
