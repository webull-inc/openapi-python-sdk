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

# coding=utf-8

from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65vents.proto\x12\x10grpc.trade.event\"t\n\x10SubscribeRequest\x12\x15\n\rsubscribeType\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x13\n\x0b\x63ontentType\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\t\x12\x10\n\x08\x61\x63\x63ounts\x18\x05 \x03(\t\"\xa6\x01\n\x11SubscribeResponse\x12.\n\teventType\x18\x01 \x01(\x0e\x32\x1b.grpc.trade.event.EventType\x12\x15\n\rsubscribeType\x18\x02 \x01(\r\x12\x13\n\x0b\x63ontentType\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\t\x12\x11\n\trequestId\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03*e\n\tEventType\x12\x14\n\x10SubscribeSuccess\x10\x00\x12\x08\n\x04Ping\x10\x01\x12\r\n\tAuthError\x10\x02\x12\x13\n\x0fNumOfConnExceed\x10\x03\x12\x14\n\x10SubscribeExpired\x10\x04\x32h\n\x0c\x45ventService\x12X\n\tSubscribe\x12\".grpc.trade.event.SubscribeRequest\x1a#.grpc.trade.event.SubscribeResponse\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENTTYPE._serialized_start=321
  _EVENTTYPE._serialized_end=422
  _SUBSCRIBEREQUEST._serialized_start=34
  _SUBSCRIBEREQUEST._serialized_end=150
  _SUBSCRIBERESPONSE._serialized_start=153
  _SUBSCRIBERESPONSE._serialized_end=319
  _EVENTSERVICE._serialized_start=424
  _EVENTSERVICE._serialized_end=528
# @@protoc_insertion_point(module_scope)
