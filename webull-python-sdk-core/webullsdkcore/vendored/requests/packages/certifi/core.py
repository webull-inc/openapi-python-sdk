# Copyright 2022 Webull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os
import warnings


class DeprecatedBundleWarning(DeprecationWarning):
    """
    The weak security bundle is being deprecated. Please bother your service
    provider to get them to stop using cross-signed roots.
    """


def where():
    f = os.path.dirname(__file__)

    return os.path.join(f, 'cacert.pem')


def old_where():
    warnings.warn(
        "The weak security bundle has been removed. certifi.old_where() is now an alias "
        "of certifi.where(). Please update your code to use certifi.where() instead. "
        "certifi.old_where() will be removed in 2018.",
        DeprecatedBundleWarning
    )
    return where()

if __name__ == '__main__':
    print(where())
