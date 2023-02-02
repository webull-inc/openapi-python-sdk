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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgateway.proto\x12\x07openapi\"a\n\rClientRequest\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.openapi.MsgType\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\"}\n\x0e\x43lientResponse\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.openapi.MsgType\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\r\x12\x0b\n\x03msg\x18\x04 \x01(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x0f\n\x07payload\x18\x06 \x01(\x0c*S\n\x07MsgType\x12\x08\n\x04Ping\x10\x00\x12\x08\n\x04Pong\x10\x01\x12\x0b\n\x07Payload\x10\x02\x12\x0c\n\x08\x43omplete\x10\x03\x12\n\n\x06\x43\x61ncel\x10\x04\x12\r\n\tDowngrade\x10\x05\x32O\n\x05Quote\x12\x46\n\rStreamRequest\x12\x16.openapi.ClientRequest\x1a\x17.openapi.ClientResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MSGTYPE._serialized_start=252
  _MSGTYPE._serialized_end=335
  _CLIENTREQUEST._serialized_start=26
  _CLIENTREQUEST._serialized_end=123
  _CLIENTRESPONSE._serialized_start=125
  _CLIENTRESPONSE._serialized_end=250
  _QUOTE._serialized_start=337
  _QUOTE._serialized_end=416
# @@protoc_insertion_point(module_scope)
