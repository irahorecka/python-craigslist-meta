black:
	black ./*.py craigslist_meta/*.py;
	rm -rf craigslist_meta/__pycache__;

flake:
	flake8 ./*.py craigslist_meta/*.py;

pylint:
	pylint ./*.py craigslist_meta/*.py;