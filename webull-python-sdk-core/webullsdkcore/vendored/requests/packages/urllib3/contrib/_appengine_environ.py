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

"""
This module provides means to detect the App Engine environment.
"""

import os


def is_appengine():
    return (is_local_appengine() or
            is_prod_appengine() or
            is_prod_appengine_mvms())


def is_appengine_sandbox():
    return is_appengine() and not is_prod_appengine_mvms()


def is_local_appengine():
    return ('APPENGINE_RUNTIME' in os.environ and
            'Development/' in os.environ['SERVER_SOFTWARE'])


def is_prod_appengine():
    return ('APPENGINE_RUNTIME' in os.environ and
            'Google App Engine/' in os.environ['SERVER_SOFTWARE'] and
            not is_prod_appengine_mvms())


def is_prod_appengine_mvms():
    return os.environ.get('GAE_VM', False) == 'true'
