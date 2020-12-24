black:
	black ./setup.py craigslist_meta/__init__.py craigslist_meta/api.py craigslist_meta/metadata.py;
	rm -rf craigslist_meta/__pycache__

flake:
	flake ./setup.py craigslist_meta/__init__.py craigslist_meta/api.py

pylint:
	pylint ./setup.py craigslist_meta/__init__.py craigslist_meta/api.py