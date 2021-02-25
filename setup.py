import craigslist_meta
from setuptools import setup, find_packages


_classifiers = [
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

if __name__ == "__main__":
    setup(
        name="python-craigslist-meta",
        version=craigslist_meta.__version__,
        author="Ira Horecka",
        author_email="ira89@icloud.com",
        url="https://github.com/irahorecka/python-craigslist-meta",
        py_modules=["craigslist_meta"],
        description="A simple API to traverse Craigslist endpoints",
        long_description=open("README.rst", encoding="utf-8").read(),
        license="MIT",
        classifiers=_classifiers,
        packages=find_packages(),
    )
