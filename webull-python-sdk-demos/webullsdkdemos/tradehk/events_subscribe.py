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
from webullsdktradehk.events.types import ORDER_STATUS_CHANGED, EVENT_TYPE_ORDER
from webullsdktradeeventscore.events_client import EventsClient

if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    region_id = "hk"
    # not necessary in production env
    optional_host = "<api_endpoint>"
    events_client = EventsClient(
        your_app_key, your_app_secret, region_id, host=optional_host)

    def my_on_events_message(event_type, subscribe_type, payload, raw_message):
        if EVENT_TYPE_ORDER == event_type and ORDER_STATUS_CHANGED == subscribe_type:
            print('----request_id:%s----' % payload['request_id'])
            print(payload['account_id'])
            print(payload['client_order_id'])
            print(payload['order_status'])
    events_client.on_events_message = my_on_events_message
    events_client.do_subscribe(["account_id_foo", "account_id_bar"])
