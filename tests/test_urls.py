import concurrent.futures
import requests
from craigslist_meta import Site


def test_urls():
    """ Test every url returns success response status code. """
    urls = tuple(get_urls())
    status_codes = map_threads(lambda url: requests.get(url).status_code, urls)
    expected_status = 200
    # assert number of responses == number of urls
    assert len(list(status_codes)) == len(urls)
    assert all(status == expected_status for status in status_codes)


def get_urls():
    """ Get every Craigslist url using craigslist_meta API. """
    all_urls = []
    for site in Site.all():
        if site.has_area():
            for area in site:
                all_urls.append(area.url)
        else:
            all_urls.append(site.url)

    return all_urls


def map_threads(func, iterable):
    """ Map function to iterable object using thread pools. """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(func, iterable)
    return result
