black:
	black --line-length=100 ./*.py ./craigslist_meta/*.py;
	rm -rf ./craigslist_meta/__pycache__;

build:
	python ./setup.py sdist

deploy:
	twine upload ./dist/*

clean:
	rm -rf ./python_craigslist_meta.egg-info ./dist ./build ./craigslist_meta/__pycache__;

flake:
	flake8 ./*.py ./craigslist_meta/*.py;

pylint:
	pylint ./*.py ./craigslist_meta/*.py;
