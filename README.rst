python-craigslist-meta
======================

|PyPI version fury.io| |PyPI pyversions|

.. |PyPI version fury.io| image:: https://badge.fury.io/py/python-craigslist-meta.svg
    :target: https://pypi.python.org/pypi/python-craigslist-meta
.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/python-craigslist-meta.svg
    :target: https://pypi.python.org/pypi/python-craigslist-meta/

Streamline your Craigslist queries with an API that traverses url endpoints.
This library serves as an addition to `pycraigslist <https://github.com/irahorecka/pycraigslist>`__ and `python-craigslist <https://github.com/juliomalegria/python-craigslist>`__.

Installation
------------

::

    pip install python-craigslist-meta

Examples
--------

Let's find every car and truck for sale around the world. ``pycraigslist`` is required for this example.

.. code:: python

    import pycraigslist
    from craigslist_meta import Site

    for site in Site.all():
        if site.has_area():
            for area in site:
                all_autos = pycraigslist.forsale.cta(site=site.key, area=area.key)
                for auto in all_autos.search():
                    print(auto)
        else:
            all_autos = pycraigslist.forsale.cta(site=site.key)
            for auto in all_autos.search():
                print(auto)


We could run the same search using ``python-craigslist``.

.. code:: python

    from craigslist import CraigslistForSale
    from craigslist_meta import Site

    for site in Site.all():
        if site.has_area():
            for area in site:
                all_autos = CraigslistForSale(site=site.key, area=area.key, category='cta')
                for auto in all_autos.get_results():
                    print(auto)
        else:
            all_autos = CraigslistForSale(site=site.key, category='cta')
            for auto in all_autos.get_results():
                    print(auto)

Let's get Craigslist urls of areas in the San Francisco Bay Area.

.. code-block:: python

    from craigslist_meta import Site

    sfbay = Site("sfbay")
    for area in sfbay:
        print(area.url)


    # https://sfbay.craigslist.org/eby/
    # https://sfbay.craigslist.org/nby/
    # https://sfbay.craigslist.org/pen/
    # https://sfbay.craigslist.org/sby/
    # ...


We can also work with countries. Let's get site keys in Germany.

.. code:: python

    from craigslist_meta import Country

    germany = Country("germany")
    for site in germany:
        print(site.key)


    # berlin
    # bremen
    # cologne
    # dresden
    # ...

Let's get titles of sites in Japan.

.. code:: python

    from craigslist_meta import Country

    japan = Country("japan")
    for site in japan:
        print(site.title)


    # 福岡
    # 広島
    # 名古屋
    # 沖縄
    # ...

Finally, we can go a step further and work with regions.

.. code:: python

    from craigslist_meta import Region

    africa = Region("africa")
    for country in africa:
        print(country.title)


    # Egypt
    # Ethiopia
    # Ghana
    # Kenya
    # ...

----

Get a list of valid keys for Region, Country, and Site by using the ``keys`` class attribute.

.. code:: python

    from craigslist_meta import Site

    print(Site.keys)


    # ['abbotsford', 'aberdeen', 'abilene', ... ]

| Similarly, get a list of children keys for Region, Country, and Site instances by using the ``children`` attribute.
| The children heirarchy is as follows: Region --> Country --> Site --> Area

.. code:: python

    from craigslist_meta import Country

    india = Country("india")
    # print site keys in India
    print(india.children)


    # ['ahmedabad', 'bangalore', 'bhubaneswar', ... ]


Contribute
----------

- `Issue Tracker <https://github.com/irahorecka/python-craigslist-meta/issues>`__
- `Source Code <https://github.com/irahorecka/python-craigslist-meta/tree/master/craigslist_meta>`__

Support
-------

If you are having issues or would like to propose a new feature, please use the `issues tracker <https://github.com/irahorecka/python-craigslist-meta/issues>`__.

License
-------

The project is licensed under the MIT license.
