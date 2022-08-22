import os
from setuptools import setup, find_packages

PACKAGE = "webullsdkquotescore"
DESCRIPTION = "The quotes core module of Webull Python SDK."
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
    "paho-mqtt==1.6.1",
    "protobuf==3.19.3",
    "webull-python-sdk-core==0.1.0"
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
    'platforms': 'any',
    'install_requires': requires 
}

setup(name='webull-python-sdk-quotes-core', **setup_args)
