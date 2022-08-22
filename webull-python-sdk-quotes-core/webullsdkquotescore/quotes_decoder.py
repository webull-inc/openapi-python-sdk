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

from webullsdkquotescore.quotes_payload_decoder import Utf8Decoder
from webullsdkquotescore.quotes_topic import QuotesTopic


class QuotesDecoder:
    def __init__(self):
        self._payload_decoders = {}
        self._default_decoder = Utf8Decoder()

    def register_payload_decoder(self, payload_type, decoder):
        self._payload_decoders[payload_type] = decoder

    def decode(self, message):
        topic = message.topic
        quotes_topic = self.decode_topic(topic)
        if quotes_topic:
            payload = message.payload
            decoded_payload = self.decode_payload(quotes_topic, payload)
            return (quotes_topic, decoded_payload)
        return None

    def decode_payload(self, quotes_topic, payload):
        payload_type = quotes_topic.data_type
        decoder = self._payload_decoders.get(payload_type)
        if decoder:
            return decoder.parse(payload)
        else:
            return self._default_decoder.parse(payload)

    def decode_topic(self, topic):
        if not topic:
            return None
        segments = topic.split("-")
        if len(segments) != 3:
            return None
        return QuotesTopic(segments[0], segments[1], segments[2])
