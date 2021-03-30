from .metadata import CRAIGSLIST, REGIONS, COUNTRIES, SITES


class classproperty(property):
    """ Allow property attribute for class methods. """

    def __get__(self, obj, objtype=None):
        return super(classproperty, self).__get__(objtype)


class Base:
    """ Base class for Region, Country, Site, and Area in api.py. """

    _selector_key = ""
    _subclass = None
    _valid_keys = {
        "region": REGIONS,
        "country": COUNTRIES,
        "site": SITES,
    }

    def __init__(self, key):
        if key not in self._valid_keys[self._selector_key]:
            raise ValueError(
                "invalid key: '%s'. See list of valid keys using the 'get_keys' method --> %s.get_keys()"
                % (key, self.__class__.__name__)
            )
        self._key = key

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self._key)

    def __iter__(self):
        """ Yield instance(s) of caller's subclass. Sublass instances are instances
        of caller's children. """
        yield from (
            self._subclass(child_key)
            for child_key in find_children(CRAIGSLIST, self._selector_key, self._key)
        )

    @classproperty
    def all(cls):
        """ Yield all instances of current class. """
        yield from (cls(key) for key in find_keys(CRAIGSLIST, cls._selector_key))

    @classproperty
    def keys(cls):
        """ Return supported keys of class. """
        return list(find_keys(CRAIGSLIST, cls._selector_key))

    @property
    def children(self):
        """ Return children keys of instance. """
        return list(find_children(CRAIGSLIST, self._selector_key, self._key))

    @property
    def key(self):
        """ Return key of instance. """
        return self._key

    @property
    def title(self):
        """ Return title of instance. """
        return find_title(CRAIGSLIST, self._selector_key, self._key)

    @property
    def url(self):
        """ Return url of instance. """
        return find_url(CRAIGSLIST, self._selector_key, self._key)


def find_keys(tree, selector):
    """ Yield all keys that match tree's 'selector'. """

    def recurse_keys(tree):
        for datum, tree in tree.items():
            """ Recurse tree and yield keys in given selector. """
            if tree["selector"] == selector:
                yield datum
            else:
                yield from recurse_keys(tree["child"])

    yield from sorted(list(set(recurse_keys(tree))))


def find_children(tree, selector, key):
    """ Yield all unique children keys that match tree's 'selector'. """

    def recurse_children(tree):
        """ Recurse tree and yield selected datum's children. """
        for datum, tree in tree.items():
            if tree["selector"] == selector and datum == key:
                yield from tree["child"].keys()
            else:
                yield from recurse_children(tree["child"])

    yield from sorted(list(set(recurse_children(tree))))


def find_title(tree, selector, key):
    """ Return "title" key value that matches tree's "selector" and datum. """

    def recurse_title(tree):
        """ Recurse tree and yield selected datum's title. """
        for datum, tree in tree.items():
            if tree["selector"] == selector and datum == key:
                yield tree["title"]
            else:
                yield from recurse_title(tree["child"])

    return next(recurse_title(tree))


def find_url(tree, selector, key):
    """ Return url that matches tree's `selector` and datum. """

    def recurse_url(tree, parent=""):
        """ Recurse tree and yield selected datum's url. """
        for datum, tree in tree.items():
            if tree["selector"] == selector and datum == key:
                yield build_url(selector, datum, parent)
            else:
                yield from recurse_url(tree["child"], datum)

    return next(recurse_url(tree))


def build_url(selector, child_key, parent_key):
    """ Return url string that's conditional to `selector` ("site" or "area"). """
    if selector == "site":
        return "https://%s.craigslist.org/" % child_key
    return "https://%s.craigslist.org/%s/" % (parent_key, child_key)
