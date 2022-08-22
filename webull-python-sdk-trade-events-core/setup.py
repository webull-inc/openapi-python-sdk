import os
from setuptools import setup, find_packages

PACKAGE = "webullsdktradeeventscore"
DESCRIPTION = "The trade events core module of Webull Python SDK."
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
    "grpcio==1.43.0",
    "grpcio-tools==1.43.0",
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

setup(name='webull-python-sdk-trade-events-core', **setup_args)
