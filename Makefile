black:
	black craigslist_meta/__init__.py craigslist_meta/api.py craigslist_meta/metadata.py;
	rm -rf craigslist_meta/__pycache__

flake:
	flake craigslist_meta/__init__.py craigslist_meta/api.py

pylint:
	pylint craigslist_meta/__init__.py craigslist_meta/api.py