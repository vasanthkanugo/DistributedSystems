# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x64\x62.proto\"\x1c\n\x0bread_db_msg\x12\r\n\x05query\x18\x01 \x01(\t\"\x1d\n\x0cwrite_db_msg\x12\r\n\x05query\x18\x01 \x01(\t\" \n\x0cresponse_msg\x12\x10\n\x08response\x18\x01 \x01(\t23\n\x07read_db\x12(\n\x07read_db\x12\x0c.read_db_msg\x1a\r.response_msg\"\x00\x32\x36\n\x08write_db\x12*\n\x08write_db\x12\r.write_db_msg\x1a\r.response_msg\"\x00\x62\x06proto3')



_READ_DB_MSG = DESCRIPTOR.message_types_by_name['read_db_msg']
_WRITE_DB_MSG = DESCRIPTOR.message_types_by_name['write_db_msg']
_RESPONSE_MSG = DESCRIPTOR.message_types_by_name['response_msg']
read_db_msg = _reflection.GeneratedProtocolMessageType('read_db_msg', (_message.Message,), {
  'DESCRIPTOR' : _READ_DB_MSG,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:read_db_msg)
  })
_sym_db.RegisterMessage(read_db_msg)

write_db_msg = _reflection.GeneratedProtocolMessageType('write_db_msg', (_message.Message,), {
  'DESCRIPTOR' : _WRITE_DB_MSG,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:write_db_msg)
  })
_sym_db.RegisterMessage(write_db_msg)

response_msg = _reflection.GeneratedProtocolMessageType('response_msg', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE_MSG,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:response_msg)
  })
_sym_db.RegisterMessage(response_msg)

_READ_DB = DESCRIPTOR.services_by_name['read_db']
_WRITE_DB = DESCRIPTOR.services_by_name['write_db']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _READ_DB_MSG._serialized_start=12
  _READ_DB_MSG._serialized_end=40
  _WRITE_DB_MSG._serialized_start=42
  _WRITE_DB_MSG._serialized_end=71
  _RESPONSE_MSG._serialized_start=73
  _RESPONSE_MSG._serialized_end=105
  _READ_DB._serialized_start=107
  _READ_DB._serialized_end=158
  _WRITE_DB._serialized_start=160
  _WRITE_DB._serialized_end=214
# @@protoc_insertion_point(module_scope)
