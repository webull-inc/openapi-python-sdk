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

import unittest

from webullsdktrade.events.types import ORDER_STATUS_CHANGED, EVENT_TYPE_ORDER
from webullsdktradeeventscore.events_client import EventsClient

your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
region_id = "hk"

endpoint = "<event_api_endpoint>"


class TestGrpcSubscribe(unittest.TestCase):
    def test_subscribe(self):
        # Create EventsClient instance
        events_client = EventsClient(your_app_key, your_app_secret, region_id)
        # For non production environment, you need to set the domain name of the subscription service through eventsclient. For example, the domain name of the UAT environment is set here
        events_client = EventsClient(your_app_key, your_app_secret, region_id,
                                     host=endpoint)

        # Set the callback function when the event data is received.
        # The data of order status change is printed here

        def my_on_events_message(event_type, subscribe_type, payload, raw_message):
            if EVENT_TYPE_ORDER == event_type and ORDER_STATUS_CHANGED == subscribe_type:
                print('----request_id:%s----' % payload['request_id'])
                print(payload['account_id'])
                print(payload['client_order_id'])
                print(payload['order_status'])

        events_client.on_events_message = my_on_events_message
        # Set the account ID to be subscribed and initiate the subscription. This method is synchronous
        events_client.do_subscribe([account_id])
