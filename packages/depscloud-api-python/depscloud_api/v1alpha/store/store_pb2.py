# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depscloud_api/v1alpha/store/store.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depscloud_api/v1alpha/store/store.proto',
  package='cloud.deps.api.v1alpha.store',
  syntax='proto3',
  serialized_options=b'Z&github.com/depscloud/api/v1alpha/store',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'depscloud_api/v1alpha/store/store.proto\x12\x1c\x63loud.deps.api.v1alpha.store\"\xa0\x01\n\tGraphItem\x12\x15\n\rgraphItemType\x18\x01 \x01(\t\x12\n\n\x02k1\x18\x02 \x01(\x0c\x12\n\n\x02k2\x18\x03 \x01(\x0c\x12\n\n\x02k3\x18\x04 \x01(\x0c\x12\x41\n\x08\x65ncoding\x18\x06 \x01(\x0e\x32/.cloud.deps.api.v1alpha.store.GraphItemEncoding\x12\x15\n\rgraphItemData\x18\x07 \x01(\x0c\"}\n\rGraphItemPair\x12\x35\n\x04\x65\x64ge\x18\x01 \x01(\x0b\x32\'.cloud.deps.api.v1alpha.store.GraphItem\x12\x35\n\x04node\x18\x02 \x01(\x0b\x32\'.cloud.deps.api.v1alpha.store.GraphItem\"D\n\nPutRequest\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.cloud.deps.api.v1alpha.store.GraphItem\"\r\n\x0bPutResponse\"G\n\rDeleteRequest\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.cloud.deps.api.v1alpha.store.GraphItem\"\x10\n\x0e\x44\x65leteResponse\"8\n\x0bListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\t\"F\n\x0cListResponse\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.cloud.deps.api.v1alpha.store.GraphItem\"-\n\x0b\x46indRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\tedgeTypes\x18\x02 \x03(\t\"J\n\x0c\x46indResponse\x12:\n\x05pairs\x18\x01 \x03(\x0b\x32+.cloud.deps.api.v1alpha.store.GraphItemPair*&\n\x11GraphItemEncoding\x12\x07\n\x03RAW\x10\x00\x12\x08\n\x04JSON\x10\x01\x32\xfc\x03\n\nGraphStore\x12Z\n\x03Put\x12(.cloud.deps.api.v1alpha.store.PutRequest\x1a).cloud.deps.api.v1alpha.store.PutResponse\x12\x63\n\x06\x44\x65lete\x12+.cloud.deps.api.v1alpha.store.DeleteRequest\x1a,.cloud.deps.api.v1alpha.store.DeleteResponse\x12]\n\x04List\x12).cloud.deps.api.v1alpha.store.ListRequest\x1a*.cloud.deps.api.v1alpha.store.ListResponse\x12\x65\n\x0c\x46indUpstream\x12).cloud.deps.api.v1alpha.store.FindRequest\x1a*.cloud.deps.api.v1alpha.store.FindResponse\x12g\n\x0e\x46indDownstream\x12).cloud.deps.api.v1alpha.store.FindRequest\x1a*.cloud.deps.api.v1alpha.store.FindResponseB(Z&github.com/depscloud/api/v1alpha/storeb\x06proto3'
)

_GRAPHITEMENCODING = _descriptor.EnumDescriptor(
  name='GraphItemEncoding',
  full_name='cloud.deps.api.v1alpha.store.GraphItemEncoding',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=792,
  serialized_end=830,
)
_sym_db.RegisterEnumDescriptor(_GRAPHITEMENCODING)

GraphItemEncoding = enum_type_wrapper.EnumTypeWrapper(_GRAPHITEMENCODING)
RAW = 0
JSON = 1



_GRAPHITEM = _descriptor.Descriptor(
  name='GraphItem',
  full_name='cloud.deps.api.v1alpha.store.GraphItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='graphItemType', full_name='cloud.deps.api.v1alpha.store.GraphItem.graphItemType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k1', full_name='cloud.deps.api.v1alpha.store.GraphItem.k1', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k2', full_name='cloud.deps.api.v1alpha.store.GraphItem.k2', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k3', full_name='cloud.deps.api.v1alpha.store.GraphItem.k3', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='cloud.deps.api.v1alpha.store.GraphItem.encoding', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graphItemData', full_name='cloud.deps.api.v1alpha.store.GraphItem.graphItemData', index=5,
      number=7, type=12, cpp_type=9, label=1,
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
  serialized_start=74,
  serialized_end=234,
)


_GRAPHITEMPAIR = _descriptor.Descriptor(
  name='GraphItemPair',
  full_name='cloud.deps.api.v1alpha.store.GraphItemPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='cloud.deps.api.v1alpha.store.GraphItemPair.edge', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node', full_name='cloud.deps.api.v1alpha.store.GraphItemPair.node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=236,
  serialized_end=361,
)


_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='cloud.deps.api.v1alpha.store.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='cloud.deps.api.v1alpha.store.PutRequest.items', index=0,
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
  serialized_start=363,
  serialized_end=431,
)


_PUTRESPONSE = _descriptor.Descriptor(
  name='PutResponse',
  full_name='cloud.deps.api.v1alpha.store.PutResponse',
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
  serialized_start=433,
  serialized_end=446,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='cloud.deps.api.v1alpha.store.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='cloud.deps.api.v1alpha.store.DeleteRequest.items', index=0,
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
  serialized_start=448,
  serialized_end=519,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='cloud.deps.api.v1alpha.store.DeleteResponse',
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
  serialized_start=521,
  serialized_end=537,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='cloud.deps.api.v1alpha.store.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='cloud.deps.api.v1alpha.store.ListRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='cloud.deps.api.v1alpha.store.ListRequest.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cloud.deps.api.v1alpha.store.ListRequest.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=539,
  serialized_end=595,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='cloud.deps.api.v1alpha.store.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='cloud.deps.api.v1alpha.store.ListResponse.items', index=0,
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
  serialized_start=597,
  serialized_end=667,
)


_FINDREQUEST = _descriptor.Descriptor(
  name='FindRequest',
  full_name='cloud.deps.api.v1alpha.store.FindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cloud.deps.api.v1alpha.store.FindRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edgeTypes', full_name='cloud.deps.api.v1alpha.store.FindRequest.edgeTypes', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=669,
  serialized_end=714,
)


_FINDRESPONSE = _descriptor.Descriptor(
  name='FindResponse',
  full_name='cloud.deps.api.v1alpha.store.FindResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pairs', full_name='cloud.deps.api.v1alpha.store.FindResponse.pairs', index=0,
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
  serialized_start=716,
  serialized_end=790,
)

_GRAPHITEM.fields_by_name['encoding'].enum_type = _GRAPHITEMENCODING
_GRAPHITEMPAIR.fields_by_name['edge'].message_type = _GRAPHITEM
_GRAPHITEMPAIR.fields_by_name['node'].message_type = _GRAPHITEM
_PUTREQUEST.fields_by_name['items'].message_type = _GRAPHITEM
_DELETEREQUEST.fields_by_name['items'].message_type = _GRAPHITEM
_LISTRESPONSE.fields_by_name['items'].message_type = _GRAPHITEM
_FINDRESPONSE.fields_by_name['pairs'].message_type = _GRAPHITEMPAIR
DESCRIPTOR.message_types_by_name['GraphItem'] = _GRAPHITEM
DESCRIPTOR.message_types_by_name['GraphItemPair'] = _GRAPHITEMPAIR
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['PutResponse'] = _PUTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['FindRequest'] = _FINDREQUEST
DESCRIPTOR.message_types_by_name['FindResponse'] = _FINDRESPONSE
DESCRIPTOR.enum_types_by_name['GraphItemEncoding'] = _GRAPHITEMENCODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphItem = _reflection.GeneratedProtocolMessageType('GraphItem', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHITEM,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.GraphItem)
  })
_sym_db.RegisterMessage(GraphItem)

GraphItemPair = _reflection.GeneratedProtocolMessageType('GraphItemPair', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHITEMPAIR,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.GraphItemPair)
  })
_sym_db.RegisterMessage(GraphItemPair)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

FindRequest = _reflection.GeneratedProtocolMessageType('FindRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDREQUEST,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.FindRequest)
  })
_sym_db.RegisterMessage(FindRequest)

FindResponse = _reflection.GeneratedProtocolMessageType('FindResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDRESPONSE,
  '__module__' : 'depscloud_api.v1alpha.store.store_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.store.FindResponse)
  })
_sym_db.RegisterMessage(FindResponse)


DESCRIPTOR._options = None

_GRAPHSTORE = _descriptor.ServiceDescriptor(
  name='GraphStore',
  full_name='cloud.deps.api.v1alpha.store.GraphStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=833,
  serialized_end=1341,
  methods=[
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='cloud.deps.api.v1alpha.store.GraphStore.Put',
    index=0,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_PUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='cloud.deps.api.v1alpha.store.GraphStore.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='cloud.deps.api.v1alpha.store.GraphStore.List',
    index=2,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindUpstream',
    full_name='cloud.deps.api.v1alpha.store.GraphStore.FindUpstream',
    index=3,
    containing_service=None,
    input_type=_FINDREQUEST,
    output_type=_FINDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindDownstream',
    full_name='cloud.deps.api.v1alpha.store.GraphStore.FindDownstream',
    index=4,
    containing_service=None,
    input_type=_FINDREQUEST,
    output_type=_FINDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRAPHSTORE)

DESCRIPTOR.services_by_name['GraphStore'] = _GRAPHSTORE

# @@protoc_insertion_point(module_scope)