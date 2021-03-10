from .metadata import CRAIGSLIST, REGIONS, COUNTRIES, SITES, AREAS


class Base:
    """ Base class for Region, Country, Site, and Area in api.py. """

    _selector_key = ""
    _subclass = None
    _valid_keys = {
        "region": REGIONS,
        "country": COUNTRIES,
        "site": SITES,
        "area": AREAS,
    }

    def __init__(self, key):
        if key not in self._valid_keys[self._selector_key]:
            raise ValueError("invalid key: '%s'" % key)
        self._key = key

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self._key)

    def __iter__(self):
        """ Yield instance(s) of caller's subclass. Sublass instances are within scope
        of caller's children. """
        yield from (
            self._subclass(child)
            for child in find_children(CRAIGSLIST, self._selector_key, self._key)
        )

    @classmethod
    def all(cls):
        """ Yield all instances of the current class. """
        yield from (cls(child) for child in find_all(CRAIGSLIST, cls._selector_key))

    @property
    def key(self):
        """ Return key of the instance. """
        return self._key

    @property
    def title(self):
        """ Return title of the instance. """
        return find_title(CRAIGSLIST, self._selector_key, self._key)

    @property
    def url(self):
        """ Return url of the instance. """
        return find_url(CRAIGSLIST, self._selector_key, self._key)


def find_all(tree, selector):
    """ Yield all keys that match tree's 'selector'. """
    for element, subtree in tree.items():
        if subtree["selector"] == selector:
            yield element
        else:
            yield from find_all(subtree["child"], selector)


def find_children(tree, selector, datum):
    """ Yield all unique children keys that match tree's 'selector'. """

    def recurse_children(tree_, selector_, datum_):
        """ Recurse tree and yield selected children. """
        for element, subtree in tree_.items():
            if subtree["selector"] == selector_ and element == datum_:
                yield from subtree["child"].keys()
            else:
                yield from recurse_children(subtree["child"], selector_, datum_)

    yield from sorted(list(set(recurse_children(tree, selector, datum))))


def find_title(tree, selector, datum):
    """ Return 'title' value that matches tree's 'selector' and element. """

    def recurse_title(tree_, selector_, datum_):
        """ Recurse tree and yield selected title. """
        for element, subtree in tree_.items():
            if subtree["selector"] == selector_ and element == datum_:
                yield subtree["title"]
            else:
                yield from recurse_title(subtree["child"], selector_, datum_)

    return list(recurse_title(tree, selector, datum)).pop(0)


def find_url(tree, selector, datum):
    """ Return url that matches tree's 'selector' and element. """

    def recurse_url(tree_, selector_, datum_, parent=""):
        """ Recurse tree and yield selected url. """
        for element, subtree in tree_.items():
            if subtree["selector"] == selector_ and element == datum_:
                yield build_url(selector_, element, parent)
            else:
                yield from recurse_url(subtree["child"], selector_, datum_, element)

    return list(recurse_url(tree, selector, datum)).pop(0)


def build_url(selector, child_key, parent_key=""):
    """ Return url string that's conditional to selector ('site' or 'area'). """
    if selector == "site":
        return "https://%s.craigslist.org/" % child_key
    return "https://%s.craigslist.org/%s/" % (parent_key, child_key)
