#!/usr/bin/python3
import setuptools
from dataserve import __version__

#To create the pypi distribution do..
#   python3 setup.py sdist bdist_wheel

with open('README.md', 'r') as fh:
    readme = fh.read()

setuptools.setup(
    name='dataserve',
    version=__version__,
    author='Brad Jascob',
    author_email='bjascob@msn.com',
    description='A module for serving up python data in a stand-alone process.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/bjascob/PythonDataServe',   
    install_requires = ['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
