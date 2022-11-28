# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8
from webullsdkcore.client import ApiClient
from webullsdkmdata.common.category import Category
from webullsdkmdata.request.get_snapshot_request import GetSnapshotRequest

if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    region_id = "hk"
    optional_api_endpoint = "<api_endpoint>"
    api_client = ApiClient(your_app_key, your_app_secret, region_id)
    request = GetSnapshotRequest()
    request.set_endpoint(optional_api_endpoint)
    request.set_category(Category.US_STOCK.name)
    request.set_symbols("AAPL")
    response = api_client.get_response(request)
    for quote_data in response.json():
        for key in quote_data.keys():
            print(key, quote_data[key], type(quote_data[key]), sep="|")
        print("-----------------------------------------")