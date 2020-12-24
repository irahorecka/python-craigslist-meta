python-craigslist-meta
======================

Streamline your Craigslist queries with an API that traverses url endpoints. This library goes hand-in-hand with `python-craigslist <https://github.com/juliomalegria/python-craigslist>`__.

Installation
------------

::

    pip install python-craigslist-meta

Examples
--------

Find cars and trucks for sale from around the world. (Note: you must have ``python-craigslist`` installed for this example)

.. code:: python

    from craigslist import CraigslistForSale
    from craigslist_meta import Site

    for site in Site.all():
        if site.has_area():
            for area in site:
                auto = CraigslistForSale(site=site.key(), area=area.key(), category='cta')
                # fetch posts from auto
        else:
            auto = CraigslistForSale(site=site.key(), category='cta')
            # fetch posts from auto

Let's get titles and urls from areas in the San Francisco Bay Area.

.. code-block:: python

    from craigslist_meta import Site

    sfbay = Site("sfbay")
    for area in sfbay:
        print(area.title(), "|", area.url())


    # East Bay Area | https://sfbay.craigslist.org/eby/
    # North Bay / Marin | https://sfbay.craigslist.org/nby/
    # Peninsula | https://sfbay.craigslist.org/pen/
    # South Bay Area | https://sfbay.craigslist.org/sby/
    # ...


We can also work with countries. Let's find site urls in Germany.

.. code:: python

    from craigslist_meta import Country

    germany = Country("germany")
    for site in germany:
        print(site.url())


    # https://berlin.craigslist.org/
    # https://bremen.craigslist.org/
    # https://cologne.craigslist.org/
    # https://dresden.craigslist.org/
    # ...

Finally, let's get url keys and titles from sites in Japan.

.. code:: python

    from craigslist_meta import Country

    japan = Country("japan")
    for site in japan:
        print(site.key(), "|", site.title())


    # fukuoka | 福岡
    # hiroshima | 広島
    # nagoya | 名古屋
    # okinawa | 沖縄
    # ...

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