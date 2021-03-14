black:
	find . -type f -name "*.py" | xargs black --line-length=100;
	find . -type d -name "__pycache__" | xargs rm -r;

flake:
	find . -type f -name "*.py" -a ! -name "metadata.py" | xargs flake8;

pylint:
	find . -type f -name "*.py" -a ! -name "metadata.py" | xargs pylint; 

pypi:
	python ./setup.py sdist;
	twine upload ./dist/*;
	rm -rf ./python_craigslist_meta.egg-info ./dist ./build;
	find . -type d -name "__pycache__" | xargs rm -r;
