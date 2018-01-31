import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="structures-and-algorithms",
    version="0.0.1",
    author="Mark Challoner",
    author_email="mark.a.r.challoner@gmail.com",
    description="A collection of data structures and algorithms.",
    license="MIT",
    keywords="example documentation tutorial",
    url="https://github.com/markchalloner/structures-and-algorithms",
    packages=['structures-and-algorithms'],
    test_suite='structures-and-algorithms.tests',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)