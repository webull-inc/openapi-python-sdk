import os
from setuptools import setup, find_packages

PACKAGE = "webullsdktradeus"
DESCRIPTION = "The us trade module of Webull Python SDK."
TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__
AUTHOR = "Webull"
AUTHOR_EMAIL = ""
URL = ""
RD_CONTENT_TYPE = "text/markdown"
LICENSE = "Apache License 2.0"

with open("README.rst") as fp:
    LONG_DESCRIPTION = fp.read()

requires = [
    "webull-python-sdk-core==0.1.2"
]

setup_args = {
    'version': VERSION,
    'author': AUTHOR,
    'author_email': AUTHOR_EMAIL,
    'description': DESCRIPTION,
    'long_description_content_type': RD_CONTENT_TYPE,
    'license': LICENSE,
    'url': URL,
    'packages': find_packages(exclude=["tests*"]),
    'include_package_data': True,
    'platforms': 'any',
    'install_requires': requires
}

setup(name='webull-python-sdk-trade-us', **setup_args)
