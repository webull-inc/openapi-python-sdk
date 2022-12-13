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

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='openapi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\x12\x07openapi\"a\n\rClientRequest\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.openapi.MsgType\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\"}\n\x0e\x43lientResponse\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.openapi.MsgType\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\r\x12\x0b\n\x03msg\x18\x04 \x01(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x0f\n\x07payload\x18\x06 \x01(\x0c*S\n\x07MsgType\x12\x08\n\x04Ping\x10\x00\x12\x08\n\x04Pong\x10\x01\x12\x0b\n\x07Payload\x10\x02\x12\x0c\n\x08\x43omplete\x10\x03\x12\n\n\x06\x43\x61ncel\x10\x04\x12\r\n\tDowngrade\x10\x05\x32O\n\x05Quote\x12\x46\n\rStreamRequest\x12\x16.openapi.ClientRequest\x1a\x17.openapi.ClientResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)

_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='openapi.MsgType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Ping', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Pong', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Payload', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Complete', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Cancel', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Downgrade', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=252,
  serialized_end=335,
)
_sym_db.RegisterEnumDescriptor(_MSGTYPE)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
Ping = 0
Pong = 1
Payload = 2
Complete = 3
Cancel = 4
Downgrade = 5



_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='openapi.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openapi.ClientRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestId', full_name='openapi.ClientRequest.requestId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='openapi.ClientRequest.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openapi.ClientRequest.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=123,
)


_CLIENTRESPONSE = _descriptor.Descriptor(
  name='ClientResponse',
  full_name='openapi.ClientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openapi.ClientResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestId', full_name='openapi.ClientResponse.requestId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='openapi.ClientResponse.code', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='openapi.ClientResponse.msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='openapi.ClientResponse.path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openapi.ClientResponse.payload', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=250,
)

_CLIENTREQUEST.fields_by_name['type'].enum_type = _MSGTYPE
_CLIENTRESPONSE.fields_by_name['type'].enum_type = _MSGTYPE
DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ClientResponse'] = _CLIENTRESPONSE
DESCRIPTOR.enum_types_by_name['MsgType'] = _MSGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:openapi.ClientRequest)
  })
_sym_db.RegisterMessage(ClientRequest)

ClientResponse = _reflection.GeneratedProtocolMessageType('ClientResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:openapi.ClientResponse)
  })
_sym_db.RegisterMessage(ClientResponse)



_QUOTE = _descriptor.ServiceDescriptor(
  name='Quote',
  full_name='openapi.Quote',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=337,
  serialized_end=416,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamRequest',
    full_name='openapi.Quote.StreamRequest',
    index=0,
    containing_service=None,
    input_type=_CLIENTREQUEST,
    output_type=_CLIENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUOTE)

DESCRIPTOR.services_by_name['Quote'] = _QUOTE

# @@protoc_insertion_point(module_scope)
