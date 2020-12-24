from . import metadata


class Base:
    """ Base class for Country, Site, and Area. """

    def __init__(self):
        self._arg = ""
        self._parent_key = ""
        self._location = {}
        self._subclass = None

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self._arg)

    def _construct(self, key, parent_key=""):
        """ Return an instance of caller's subclass if it exists. """
        if isinstance(self._location["scope"], dict):
            return self._subclass(
                self._location["scope"], scope=key, parent_key=parent_key
            )
        return None

    def _construct_all(self, parent_key=""):
        """ Yield instances of every subclass in its category. """
        try:
            yield from (
                self._construct(key, parent_key=parent_key)
                for key in self._location["scope"]
            )
        except KeyError:
            yield from ()

    def key(self):
        """ Return Craigslist url key of the instance. """
        return self._arg

    def title(self):
        """ Return Craigslist title of the instance. """
        return self._location["title"]


class Country(Base):
    """ Parse Craigslist by country. """

    def __init__(self, country):
        super().__init__()
        self._arg = country
        self._location = metadata.COUNTRY[country]
        self._subclass = Site

    def __iter__(self):
        """ Yield Site instances within country. """
        yield from self._construct_all()

    def site(self, site):
        """ Constructor for a Site instance within country's boundaries. """
        return self._construct(site)

    @classmethod
    def all(cls):
        """ Yield instances of every Country on Craigslist. """
        yield from (cls(key) for key in metadata.COUNTRY)


class Site(Base):
    """ Parse Craiglist sites. """

    def __init__(self, site, **kwargs):
        super().__init__()
        # Site provides two entry points, one through Country.site as a dict
        # (Base._construct(site_dict, scope=site_key)) and one through Site(site_key) as a str.
        if isinstance(site, str):
            self._arg = site
            self._location = metadata.SITE[site]
        else:
            # site is type dict
            site_key = kwargs.get("scope")
            self._arg = site_key
            self._location = site[site_key]

        self._subclass = Area

    def __iter__(self):
        """ Yield Area instances within site. """
        yield from self._construct_all(parent_key=self._arg)

    def area(self, area):
        """ Constructor for Area instances within site's boundaries. """
        return self._construct(area, parent_key=self._arg)

    def has_area(self):
        """ Boolean value for if site has areas. For example, 'sfbay' has areas,
        'monterey' does not. """
        return bool(self._location.get("scope"))

    def url(self):
        """ Return Craigslist url of site. """
        return "https://{}.craigslist.org/".format(self._arg)

    @classmethod
    def all(cls):
        """ Yield instances of every Site on Craigslist. """
        yield from (cls(key) for key in metadata.SITE)


class Area(Base):
    """ Parse Craigslist areas within a site. """

    def __init__(self, area, **kwargs):
        super().__init__()
        self._arg = kwargs["scope"]
        self._parent_key = kwargs["parent_key"]
        self._location = area[kwargs["scope"]]

    def url(self):
        """ Return Craigslist url of area. """
        return "https://{}.craigslist.org/{}/".format(self._parent_key, self._arg)
