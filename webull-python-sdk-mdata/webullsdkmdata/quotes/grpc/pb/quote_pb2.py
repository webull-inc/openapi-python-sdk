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

# source: quote.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='quote.proto',
  package='openapi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bquote.proto\x12\x07openapi\"2\n\rTickerRequest\x12\x0f\n\x07symbols\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"=\n\x0eTickerResponse\x12+\n\x06result\x18\x01 \x03(\x0b\x32\x1b.openapi.InstrumentResponse\"r\n\x12InstrumentResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\x12\x15\n\rexchange_code\x18\x04 \x01(\t\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\"P\n\x0b\x42\x61rsRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x10\n\x08timespan\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\t\"4\n\x0c\x42\x61rsResponse\x12$\n\x06result\x18\x01 \x03(\x0b\x32\x14.openapi.BarResponse\"c\n\x0b\x42\x61rResponse\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\t\x12\r\n\x05\x63lose\x18\x03 \x01(\t\x12\x0c\n\x04high\x18\x04 \x01(\t\x12\x0b\n\x03low\x18\x05 \x01(\t\x12\x0e\n\x06volume\x18\x06 \x01(\t\"2\n\rQuotesRequest\x12\x0f\n\x07symbols\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\">\n\x0eQuotesResponse\x12,\n\x06result\x18\x01 \x03(\x0b\x32\x1c.openapi.ReferentialResponse\"\xbe\x02\n\x13ReferentialResponse\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\t\x12\x0c\n\x04high\x18\x04 \x01(\t\x12\x0b\n\x03low\x18\x05 \x01(\t\x12\x11\n\tpre_close\x18\x06 \x01(\t\x12\x0e\n\x06volume\x18\x07 \x01(\t\x12\x0e\n\x06\x63hange\x18\x08 \x01(\t\x12\x14\n\x0c\x63hange_ratio\x18\t \x01(\t\x12\x0b\n\x03\x61sk\x18\n \x01(\t\x12\x10\n\x08\x61sk_size\x18\x0b \x01(\t\x12\x0b\n\x03\x62id\x18\x0c \x01(\t\x12\x10\n\x08\x62id_size\x18\r \x01(\t\x12\r\n\x05\x64\x65lta\x18\x0e \x01(\t\x12\r\n\x05gamma\x18\x0f \x01(\t\x12\r\n\x05theta\x18\x10 \x01(\t\x12\x0c\n\x04vega\x18\x11 \x01(\t\x12\x0b\n\x03rho\x18\x12 \x01(\t\x12\x10\n\x08imp_volt\x18\x13 \x01(\t\"\x1e\n\rTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t\"p\n\x10SubscribeRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x11\n\tsub_types\x18\x04 \x03(\t\x12\x17\n\x0funsubscribe_all\x18\x05 \x01(\t\"\x13\n\x11SubscribeResponseb\x06proto3'
)




_TICKERREQUEST = _descriptor.Descriptor(
  name='TickerRequest',
  full_name='openapi.TickerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbols', full_name='openapi.TickerRequest.symbols', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='openapi.TickerRequest.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=24,
  serialized_end=74,
)


_TICKERRESPONSE = _descriptor.Descriptor(
  name='TickerResponse',
  full_name='openapi.TickerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='openapi.TickerResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=76,
  serialized_end=137,
)


_INSTRUMENTRESPONSE = _descriptor.Descriptor(
  name='InstrumentResponse',
  full_name='openapi.InstrumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openapi.InstrumentResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='openapi.InstrumentResponse.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instrument_id', full_name='openapi.InstrumentResponse.instrument_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange_code', full_name='openapi.InstrumentResponse.exchange_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='openapi.InstrumentResponse.currency', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=139,
  serialized_end=253,
)


_BARSREQUEST = _descriptor.Descriptor(
  name='BarsRequest',
  full_name='openapi.BarsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='openapi.BarsRequest.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='openapi.BarsRequest.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timespan', full_name='openapi.BarsRequest.timespan', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='openapi.BarsRequest.count', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=255,
  serialized_end=335,
)


_BARSRESPONSE = _descriptor.Descriptor(
  name='BarsResponse',
  full_name='openapi.BarsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='openapi.BarsResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=337,
  serialized_end=389,
)


_BARRESPONSE = _descriptor.Descriptor(
  name='BarResponse',
  full_name='openapi.BarResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='openapi.BarResponse.time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open', full_name='openapi.BarResponse.open', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close', full_name='openapi.BarResponse.close', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high', full_name='openapi.BarResponse.high', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low', full_name='openapi.BarResponse.low', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='openapi.BarResponse.volume', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=391,
  serialized_end=490,
)


_QUOTESREQUEST = _descriptor.Descriptor(
  name='QuotesRequest',
  full_name='openapi.QuotesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbols', full_name='openapi.QuotesRequest.symbols', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='openapi.QuotesRequest.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=492,
  serialized_end=542,
)


_QUOTESRESPONSE = _descriptor.Descriptor(
  name='QuotesResponse',
  full_name='openapi.QuotesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='openapi.QuotesResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=544,
  serialized_end=606,
)


_REFERENTIALRESPONSE = _descriptor.Descriptor(
  name='ReferentialResponse',
  full_name='openapi.ReferentialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='openapi.ReferentialResponse.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='openapi.ReferentialResponse.price', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open', full_name='openapi.ReferentialResponse.open', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high', full_name='openapi.ReferentialResponse.high', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low', full_name='openapi.ReferentialResponse.low', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pre_close', full_name='openapi.ReferentialResponse.pre_close', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='openapi.ReferentialResponse.volume', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change', full_name='openapi.ReferentialResponse.change', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_ratio', full_name='openapi.ReferentialResponse.change_ratio', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask', full_name='openapi.ReferentialResponse.ask', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_size', full_name='openapi.ReferentialResponse.ask_size', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid', full_name='openapi.ReferentialResponse.bid', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_size', full_name='openapi.ReferentialResponse.bid_size', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delta', full_name='openapi.ReferentialResponse.delta', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='openapi.ReferentialResponse.gamma', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='theta', full_name='openapi.ReferentialResponse.theta', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vega', full_name='openapi.ReferentialResponse.vega', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rho', full_name='openapi.ReferentialResponse.rho', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imp_volt', full_name='openapi.ReferentialResponse.imp_volt', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=609,
  serialized_end=927,
)


_TOKENRESPONSE = _descriptor.Descriptor(
  name='TokenResponse',
  full_name='openapi.TokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='openapi.TokenResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=929,
  serialized_end=959,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='openapi.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='openapi.SubscribeRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbols', full_name='openapi.SubscribeRequest.symbols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='openapi.SubscribeRequest.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_types', full_name='openapi.SubscribeRequest.sub_types', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unsubscribe_all', full_name='openapi.SubscribeRequest.unsubscribe_all', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=961,
  serialized_end=1073,
)


_SUBSCRIBERESPONSE = _descriptor.Descriptor(
  name='SubscribeResponse',
  full_name='openapi.SubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1075,
  serialized_end=1094,
)

_TICKERRESPONSE.fields_by_name['result'].message_type = _INSTRUMENTRESPONSE
_BARSRESPONSE.fields_by_name['result'].message_type = _BARRESPONSE
_QUOTESRESPONSE.fields_by_name['result'].message_type = _REFERENTIALRESPONSE
DESCRIPTOR.message_types_by_name['TickerRequest'] = _TICKERREQUEST
DESCRIPTOR.message_types_by_name['TickerResponse'] = _TICKERRESPONSE
DESCRIPTOR.message_types_by_name['InstrumentResponse'] = _INSTRUMENTRESPONSE
DESCRIPTOR.message_types_by_name['BarsRequest'] = _BARSREQUEST
DESCRIPTOR.message_types_by_name['BarsResponse'] = _BARSRESPONSE
DESCRIPTOR.message_types_by_name['BarResponse'] = _BARRESPONSE
DESCRIPTOR.message_types_by_name['QuotesRequest'] = _QUOTESREQUEST
DESCRIPTOR.message_types_by_name['QuotesResponse'] = _QUOTESRESPONSE
DESCRIPTOR.message_types_by_name['ReferentialResponse'] = _REFERENTIALRESPONSE
DESCRIPTOR.message_types_by_name['TokenResponse'] = _TOKENRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeResponse'] = _SUBSCRIBERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TickerRequest = _reflection.GeneratedProtocolMessageType('TickerRequest', (_message.Message,), {
  'DESCRIPTOR' : _TICKERREQUEST,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.TickerRequest)
  })
_sym_db.RegisterMessage(TickerRequest)

TickerResponse = _reflection.GeneratedProtocolMessageType('TickerResponse', (_message.Message,), {
  'DESCRIPTOR' : _TICKERRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.TickerResponse)
  })
_sym_db.RegisterMessage(TickerResponse)

InstrumentResponse = _reflection.GeneratedProtocolMessageType('InstrumentResponse', (_message.Message,), {
  'DESCRIPTOR' : _INSTRUMENTRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.InstrumentResponse)
  })
_sym_db.RegisterMessage(InstrumentResponse)

BarsRequest = _reflection.GeneratedProtocolMessageType('BarsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BARSREQUEST,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.BarsRequest)
  })
_sym_db.RegisterMessage(BarsRequest)

BarsResponse = _reflection.GeneratedProtocolMessageType('BarsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BARSRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.BarsResponse)
  })
_sym_db.RegisterMessage(BarsResponse)

BarResponse = _reflection.GeneratedProtocolMessageType('BarResponse', (_message.Message,), {
  'DESCRIPTOR' : _BARRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.BarResponse)
  })
_sym_db.RegisterMessage(BarResponse)

QuotesRequest = _reflection.GeneratedProtocolMessageType('QuotesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUOTESREQUEST,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.QuotesRequest)
  })
_sym_db.RegisterMessage(QuotesRequest)

QuotesResponse = _reflection.GeneratedProtocolMessageType('QuotesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUOTESRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.QuotesResponse)
  })
_sym_db.RegisterMessage(QuotesResponse)

ReferentialResponse = _reflection.GeneratedProtocolMessageType('ReferentialResponse', (_message.Message,), {
  'DESCRIPTOR' : _REFERENTIALRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.ReferentialResponse)
  })
_sym_db.RegisterMessage(ReferentialResponse)

TokenResponse = _reflection.GeneratedProtocolMessageType('TokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENRESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.TokenResponse)
  })
_sym_db.RegisterMessage(TokenResponse)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeResponse = _reflection.GeneratedProtocolMessageType('SubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERESPONSE,
  '__module__' : 'quote_pb2'
  # @@protoc_insertion_point(class_scope:openapi.SubscribeResponse)
  })
_sym_db.RegisterMessage(SubscribeResponse)


# @@protoc_insertion_point(module_scope)
