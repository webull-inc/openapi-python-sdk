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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"A\n\x05\x42\x61sic\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"\xb6\x01\n\x08Snapshot\x12\x15\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x06.Basic\x12\x12\n\ntrade_time\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\t\x12\x0c\n\x04open\x18\x04 \x01(\t\x12\x0c\n\x04high\x18\x05 \x01(\t\x12\x0b\n\x03low\x18\x06 \x01(\t\x12\x11\n\tpre_close\x18\x07 \x01(\t\x12\x0e\n\x06volume\x18\x08 \x01(\t\x12\x0e\n\x06\x63hange\x18\t \x01(\t\x12\x14\n\x0c\x63hange_ratio\x18\n \x01(\t\"L\n\x05Quote\x12\x15\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x06.Basic\x12\x15\n\x04\x61sks\x18\x02 \x03(\x0b\x32\x07.AskBid\x12\x15\n\x04\x62ids\x18\x03 \x03(\x0b\x32\x07.AskBid\"X\n\x04Tick\x12\x15\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x06.Basic\x12\x0c\n\x04time\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\t\x12\x0e\n\x06volume\x18\x04 \x01(\t\x12\x0c\n\x04side\x18\x05 \x01(\t\"U\n\x06\x41skBid\x12\r\n\x05price\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\t\x12\x15\n\x05order\x18\x03 \x03(\x0b\x32\x06.Order\x12\x17\n\x06\x62roker\x18\x04 \x03(\x0b\x32\x07.Broker\"#\n\x05Order\x12\x0c\n\x04mpid\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\t\"#\n\x06\x42roker\x12\x0b\n\x03\x62id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BASIC._serialized_start=17
  _BASIC._serialized_end=82
  _SNAPSHOT._serialized_start=85
  _SNAPSHOT._serialized_end=267
  _QUOTE._serialized_start=269
  _QUOTE._serialized_end=345
  _TICK._serialized_start=347
  _TICK._serialized_end=435
  _ASKBID._serialized_start=437
  _ASKBID._serialized_end=522
  _ORDER._serialized_start=524
  _ORDER._serialized_end=559
  _BROKER._serialized_start=561
  _BROKER._serialized_end=596
# @@protoc_insertion_point(module_scope)
