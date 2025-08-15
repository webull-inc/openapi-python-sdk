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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bquote.proto\x12\x07openapi\"6\n\x11InstrumentRequest\x12\x0f\n\x07symbols\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"9\n\x12InstrumentResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.openapi.Instrument\"j\n\nInstrument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\x12\x15\n\rexchange_code\x18\x04 \x01(\t\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\"\x86\x01\n\x0b\x42\x61rsRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x10\n\x08timespan\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\t\x12\x1a\n\x12real_time_required\x18\x05 \x01(\t\x12\x18\n\x10trading_sessions\x18\x06 \x01(\t\"S\n\x0c\x42\x61rsResponse\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12\x1c\n\x06result\x18\x03 \x03(\x0b\x32\x0c.openapi.Bar\"[\n\x03\x42\x61r\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\t\x12\r\n\x05\x63lose\x18\x03 \x01(\t\x12\x0c\n\x04high\x18\x04 \x01(\t\x12\x0b\n\x03low\x18\x05 \x01(\t\x12\x0e\n\x06volume\x18\x06 \x01(\t\"\x8c\x01\n\x10\x42\x61tchBarsRequest\x12\x0f\n\x07symbols\x18\x01 \x03(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x10\n\x08timespan\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x12\x1a\n\x12real_time_required\x18\x05 \x01(\t\x12\x18\n\x10trading_sessions\x18\x06 \x03(\t\":\n\x11\x42\x61tchBarsResponse\x12%\n\x06result\x18\x01 \x03(\x0b\x32\x15.openapi.BarsResponse\"4\n\x0fSnapshotRequest\x12\x0f\n\x07symbols\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"5\n\x10SnapshotResponse\x12!\n\x06result\x18\x01 \x03(\x0b\x32\x11.openapi.Snapshot\"\xc6\x01\n\x08Snapshot\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12\x12\n\ntrade_time\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\x12\x0c\n\x04open\x18\x05 \x01(\t\x12\x0c\n\x04high\x18\x06 \x01(\t\x12\x0b\n\x03low\x18\x07 \x01(\t\x12\x11\n\tpre_close\x18\x08 \x01(\t\x12\x0e\n\x06volume\x18\t \x01(\t\x12\x0e\n\x06\x63hange\x18\n \x01(\t\x12\x14\n\x0c\x63hange_ratio\x18\x0b \x01(\t\"\x1e\n\rTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t\"p\n\x10SubscribeRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x11\n\tsub_types\x18\x04 \x03(\t\x12\x17\n\x0funsubscribe_all\x18\x05 \x01(\t\"\x13\n\x11SubscribeResponse\"0\n\x0cQuoteRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"t\n\rQuoteResponse\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12\x1d\n\x04\x61sks\x18\x03 \x03(\x0b\x32\x0f.openapi.AskBid\x12\x1d\n\x04\x62ids\x18\x04 \x03(\x0b\x32\x0f.openapi.AskBid\"e\n\x06\x41skBid\x12\r\n\x05price\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\t\x12\x1d\n\x05order\x18\x03 \x03(\x0b\x32\x0e.openapi.Order\x12\x1f\n\x06\x62roker\x18\x04 \x03(\x0b\x32\x0f.openapi.Broker\"#\n\x05Order\x12\x0c\n\x04mpid\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\t\"#\n\x06\x42roker\x12\x0b\n\x03\x62id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\">\n\x0bTickRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\t\"T\n\x0cTickResponse\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12\x1d\n\x06result\x18\x03 \x03(\x0b\x32\r.openapi.Tick\"A\n\x04Tick\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\x0e\n\x06volume\x18\x03 \x01(\t\x12\x0c\n\x04side\x18\x04 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'quote_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INSTRUMENTREQUEST._serialized_start=24
  _INSTRUMENTREQUEST._serialized_end=78
  _INSTRUMENTRESPONSE._serialized_start=80
  _INSTRUMENTRESPONSE._serialized_end=137
  _INSTRUMENT._serialized_start=139
  _INSTRUMENT._serialized_end=245
  _BARSREQUEST._serialized_start=248
  _BARSREQUEST._serialized_end=382
  _BARSRESPONSE._serialized_start=384
  _BARSRESPONSE._serialized_end=467
  _BAR._serialized_start=469
  _BAR._serialized_end=560
  _BATCHBARSREQUEST._serialized_start=563
  _BATCHBARSREQUEST._serialized_end=703
  _BATCHBARSRESPONSE._serialized_start=705
  _BATCHBARSRESPONSE._serialized_end=763
  _SNAPSHOTREQUEST._serialized_start=765
  _SNAPSHOTREQUEST._serialized_end=817
  _SNAPSHOTRESPONSE._serialized_start=819
  _SNAPSHOTRESPONSE._serialized_end=872
  _SNAPSHOT._serialized_start=875
  _SNAPSHOT._serialized_end=1073
  _TOKENRESPONSE._serialized_start=1075
  _TOKENRESPONSE._serialized_end=1105
  _SUBSCRIBEREQUEST._serialized_start=1107
  _SUBSCRIBEREQUEST._serialized_end=1219
  _SUBSCRIBERESPONSE._serialized_start=1221
  _SUBSCRIBERESPONSE._serialized_end=1240
  _QUOTEREQUEST._serialized_start=1242
  _QUOTEREQUEST._serialized_end=1290
  _QUOTERESPONSE._serialized_start=1292
  _QUOTERESPONSE._serialized_end=1408
  _ASKBID._serialized_start=1410
  _ASKBID._serialized_end=1511
  _ORDER._serialized_start=1513
  _ORDER._serialized_end=1548
  _BROKER._serialized_start=1550
  _BROKER._serialized_end=1585
  _TICKREQUEST._serialized_start=1587
  _TICKREQUEST._serialized_end=1649
  _TICKRESPONSE._serialized_start=1651
  _TICKRESPONSE._serialized_end=1735
  _TICK._serialized_start=1737
  _TICK._serialized_end=1802
# @@protoc_insertion_point(module_scope)
