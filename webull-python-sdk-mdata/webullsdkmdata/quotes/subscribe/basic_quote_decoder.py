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

from webullsdkmdata.quotes.subscribe.basic_quote_result import BasicQuoteResult
from webullsdkmdata.quotes.subscribe.message_pb2 import QuoteData
from webullsdkquotescore.quotes_payload_decoder import BaseQuotesPayloadDecoder


class BasicQuoteDecoder(BaseQuotesPayloadDecoder):
    def __init__(self):
        super().__init__()

    def parse(self, payload):
        quote = QuoteData()
        quote.ParseFromString(payload)
        return BasicQuoteResult(quote)
