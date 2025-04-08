import os
from setuptools import setup, find_packages

# for resolving grpc cython libs installation issue: https://github.com/grpc/grpc/issues/25082
if hasattr(os,"uname") and os.uname().machine == 'arm64' and os.uname().sysname == 'Darwin':
    os.system("export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1")
    os.system("export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1")

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
    "grpcio==1.51.1",
    "grpcio-tools==1.51.1",
    "protobuf==4.21.12",
    "webull-python-sdk-core==0.1.12"
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
