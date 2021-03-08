from .metadata import CRAIGSLIST


class Base:
    """ Base class for `Continent`, `Country`, `Site`, and `Area`. """

    _selector_key = ""
    _subclass_selector_key = ""
    _subclass = None

    def __init__(self):
        self._key = ""

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self._key)

    def __len__(self):
        return len(self._unique_class_keys(self._subclass_selector_key, self._key))

    def __iter__(self):
        """ Yield instance(s) of caller's subclass if it exists.
        Sublass instances are within scope of the caller's instance; for example,
        `Continent('africa')` will yield all `Country` instances that are in Africa. """
        return self._iter_class(self._subclass, self._subclass_selector_key, key=self._key)

    @classmethod
    def _iter_class(cls, _class, selector_key, key=""):
        """ Yield instances of `_class` instantiated by `key`, or if an empty string,
        all instances of `selector_key`. """
        yield from (_class(class_key) for class_key in cls._unique_class_keys(selector_key, key))

    @classmethod
    def _unique_class_keys(cls, selector_key, key):
        """ Return a unique list of class instantiation `key`s as specified by `selector_key`.
        For example, if our `selector_key` is 'country' and  `key` is 'japan', we'll return ['japan'],
        rather a list of eight `japan`s. If `key` is an empty string, return a unique list of keys
        for all values of `selector_key`["key"]. """
        return list(
            {
                region[selector_key]["key"]
                for region in cls._filter_tree(key)
                # determine if caller-specified `selector_key` in current instance's `_selector_key`
                if region.get(selector_key)
            }
        )

    @classmethod
    def _filter_tree(cls, key):
        """ Yield a sequence of dictionaries that fulfills the instance's filter as determined
        by `key`. For example, if we are in the `Continent` class, and `key` is 'africa', we'll
        yield a dict iterable where the 'continent' key has value 'africa' in `CRAIGSLIST`. """
        yield from filter(
            lambda leaf: leaf.get(cls._selector_key) and leaf[cls._selector_key]["key"] == key
            if key
            else leaf[cls._selector_key]["key"],
            CRAIGSLIST,
        )

    @classmethod
    def all(cls):
        """ Return all instances of the current class. """
        yield from cls._iter_class(cls, cls._selector_key)

    @property
    def key(self):
        """ Return key of the instance. """
        return self._key

    @property
    def title(self):
        """ Return title of the instance. """
        return self._search_tree("title")

    def _search_tree(self, key):
        """ Return value for `key` within the instance's filtered values. """
        try:
            return next(self._filter_tree(self._key))[self._selector_key].get(key)
        except StopIteration:
            return None
