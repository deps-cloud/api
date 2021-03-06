# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graphstore/api/v1beta/graphstore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='graphstore/api/v1beta/graphstore.proto',
  package='graphstore.api.v1beta',
  syntax='proto3',
  serialized_options=b'Z*github.com/depscloud/api/v1beta/graphstore',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&graphstore/api/v1beta/graphstore.proto\x12\x15graphstore.api.v1beta\x1a\x19google/protobuf/any.proto\"7\n\x04Node\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\"\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"Y\n\x04\x45\x64ge\x12\x10\n\x08\x66rom_key\x18\x01 \x01(\x0c\x12\x0e\n\x06to_key\x18\x02 \x01(\x0c\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\"\n\x04\x62ody\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"d\n\nPutRequest\x12*\n\x05nodes\x18\x01 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12*\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Edge\"\r\n\x0bPutResponse\"g\n\rDeleteRequest\x12*\n\x05nodes\x18\x01 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12*\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Edge\"\x10\n\x0e\x44\x65leteResponse\"R\n\x0bListRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0c\n\x04kind\x18\x04 \x01(\t\"\x7f\n\x0cListResponse\x12\x17\n\x0fnext_page_token\x18\x01 \x01(\t\x12*\n\x05nodes\x18\x02 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12*\n\x05\x65\x64ges\x18\x03 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Edge\"a\n\x08Neighbor\x12)\n\x04node\x18\x01 \x01(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12*\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x1b.graphstore.api.v1beta.Edge\"0\n\nEdgeFilter\x12\"\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"\xc4\x01\n\x10NeighborsRequest\x12)\n\x04node\x18\x01 \x01(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12)\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12\'\n\x02to\x18\x03 \x01(\x0b\x32\x1b.graphstore.api.v1beta.Node\x12\x31\n\x06\x66ilter\x18\x04 \x03(\x0b\x32!.graphstore.api.v1beta.EdgeFilter\"G\n\x11NeighborsResponse\x12\x32\n\tneighbors\x18\x01 \x03(\x0b\x32\x1f.graphstore.api.v1beta.Neighbor\"[\n\x0fTraverseRequest\x12\x0e\n\x06\x63\x61ncel\x18\x01 \x01(\x08\x12\x38\n\x07request\x18\x02 \x01(\x0b\x32\'.graphstore.api.v1beta.NeighborsRequest\"\x88\x01\n\x10TraverseResponse\x12\x38\n\x07request\x18\x01 \x01(\x0b\x32\'.graphstore.api.v1beta.NeighborsRequest\x12:\n\x08response\x18\x02 \x01(\x0b\x32(.graphstore.api.v1beta.NeighborsResponse2\xc3\x03\n\nGraphStore\x12L\n\x03Put\x12!.graphstore.api.v1beta.PutRequest\x1a\".graphstore.api.v1beta.PutResponse\x12U\n\x06\x44\x65lete\x12$.graphstore.api.v1beta.DeleteRequest\x1a%.graphstore.api.v1beta.DeleteResponse\x12O\n\x04List\x12\".graphstore.api.v1beta.ListRequest\x1a#.graphstore.api.v1beta.ListResponse\x12^\n\tNeighbors\x12\'.graphstore.api.v1beta.NeighborsRequest\x1a(.graphstore.api.v1beta.NeighborsResponse\x12_\n\x08Traverse\x12&.graphstore.api.v1beta.TraverseRequest\x1a\'.graphstore.api.v1beta.TraverseResponse(\x01\x30\x01\x42,Z*github.com/depscloud/api/v1beta/graphstoreb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='graphstore.api.v1beta.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='graphstore.api.v1beta.Node.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='graphstore.api.v1beta.Node.body', index=1,
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
  serialized_start=92,
  serialized_end=147,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='graphstore.api.v1beta.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_key', full_name='graphstore.api.v1beta.Edge.from_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_key', full_name='graphstore.api.v1beta.Edge.to_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='graphstore.api.v1beta.Edge.key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='graphstore.api.v1beta.Edge.body', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=149,
  serialized_end=238,
)


_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='graphstore.api.v1beta.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='graphstore.api.v1beta.PutRequest.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edges', full_name='graphstore.api.v1beta.PutRequest.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=240,
  serialized_end=340,
)


_PUTRESPONSE = _descriptor.Descriptor(
  name='PutResponse',
  full_name='graphstore.api.v1beta.PutResponse',
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
  serialized_start=342,
  serialized_end=355,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='graphstore.api.v1beta.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='graphstore.api.v1beta.DeleteRequest.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edges', full_name='graphstore.api.v1beta.DeleteRequest.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=357,
  serialized_end=460,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='graphstore.api.v1beta.DeleteResponse',
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
  serialized_start=462,
  serialized_end=478,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='graphstore.api.v1beta.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='graphstore.api.v1beta.ListRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='graphstore.api.v1beta.ListRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='graphstore.api.v1beta.ListRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='graphstore.api.v1beta.ListRequest.kind', index=3,
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
  serialized_start=480,
  serialized_end=562,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='graphstore.api.v1beta.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='graphstore.api.v1beta.ListResponse.next_page_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='graphstore.api.v1beta.ListResponse.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edges', full_name='graphstore.api.v1beta.ListResponse.edges', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=564,
  serialized_end=691,
)


_NEIGHBOR = _descriptor.Descriptor(
  name='Neighbor',
  full_name='graphstore.api.v1beta.Neighbor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='graphstore.api.v1beta.Neighbor.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edges', full_name='graphstore.api.v1beta.Neighbor.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=693,
  serialized_end=790,
)


_EDGEFILTER = _descriptor.Descriptor(
  name='EdgeFilter',
  full_name='graphstore.api.v1beta.EdgeFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='graphstore.api.v1beta.EdgeFilter.body', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=792,
  serialized_end=840,
)


_NEIGHBORSREQUEST = _descriptor.Descriptor(
  name='NeighborsRequest',
  full_name='graphstore.api.v1beta.NeighborsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='graphstore.api.v1beta.NeighborsRequest.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from', full_name='graphstore.api.v1beta.NeighborsRequest.from', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='graphstore.api.v1beta.NeighborsRequest.to', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='graphstore.api.v1beta.NeighborsRequest.filter', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=843,
  serialized_end=1039,
)


_NEIGHBORSRESPONSE = _descriptor.Descriptor(
  name='NeighborsResponse',
  full_name='graphstore.api.v1beta.NeighborsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='neighbors', full_name='graphstore.api.v1beta.NeighborsResponse.neighbors', index=0,
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
  serialized_start=1041,
  serialized_end=1112,
)


_TRAVERSEREQUEST = _descriptor.Descriptor(
  name='TraverseRequest',
  full_name='graphstore.api.v1beta.TraverseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cancel', full_name='graphstore.api.v1beta.TraverseRequest.cancel', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='graphstore.api.v1beta.TraverseRequest.request', index=1,
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
  serialized_start=1114,
  serialized_end=1205,
)


_TRAVERSERESPONSE = _descriptor.Descriptor(
  name='TraverseResponse',
  full_name='graphstore.api.v1beta.TraverseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='graphstore.api.v1beta.TraverseResponse.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='graphstore.api.v1beta.TraverseResponse.response', index=1,
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
  serialized_start=1208,
  serialized_end=1344,
)

_NODE.fields_by_name['body'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EDGE.fields_by_name['body'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_PUTREQUEST.fields_by_name['nodes'].message_type = _NODE
_PUTREQUEST.fields_by_name['edges'].message_type = _EDGE
_DELETEREQUEST.fields_by_name['nodes'].message_type = _NODE
_DELETEREQUEST.fields_by_name['edges'].message_type = _EDGE
_LISTRESPONSE.fields_by_name['nodes'].message_type = _NODE
_LISTRESPONSE.fields_by_name['edges'].message_type = _EDGE
_NEIGHBOR.fields_by_name['node'].message_type = _NODE
_NEIGHBOR.fields_by_name['edges'].message_type = _EDGE
_EDGEFILTER.fields_by_name['body'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_NEIGHBORSREQUEST.fields_by_name['node'].message_type = _NODE
_NEIGHBORSREQUEST.fields_by_name['from'].message_type = _NODE
_NEIGHBORSREQUEST.fields_by_name['to'].message_type = _NODE
_NEIGHBORSREQUEST.fields_by_name['filter'].message_type = _EDGEFILTER
_NEIGHBORSRESPONSE.fields_by_name['neighbors'].message_type = _NEIGHBOR
_TRAVERSEREQUEST.fields_by_name['request'].message_type = _NEIGHBORSREQUEST
_TRAVERSERESPONSE.fields_by_name['request'].message_type = _NEIGHBORSREQUEST
_TRAVERSERESPONSE.fields_by_name['response'].message_type = _NEIGHBORSRESPONSE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['PutResponse'] = _PUTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['Neighbor'] = _NEIGHBOR
DESCRIPTOR.message_types_by_name['EdgeFilter'] = _EDGEFILTER
DESCRIPTOR.message_types_by_name['NeighborsRequest'] = _NEIGHBORSREQUEST
DESCRIPTOR.message_types_by_name['NeighborsResponse'] = _NEIGHBORSRESPONSE
DESCRIPTOR.message_types_by_name['TraverseRequest'] = _TRAVERSEREQUEST
DESCRIPTOR.message_types_by_name['TraverseResponse'] = _TRAVERSERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.Node)
  })
_sym_db.RegisterMessage(Node)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), {
  'DESCRIPTOR' : _EDGE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.Edge)
  })
_sym_db.RegisterMessage(Edge)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

Neighbor = _reflection.GeneratedProtocolMessageType('Neighbor', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBOR,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.Neighbor)
  })
_sym_db.RegisterMessage(Neighbor)

EdgeFilter = _reflection.GeneratedProtocolMessageType('EdgeFilter', (_message.Message,), {
  'DESCRIPTOR' : _EDGEFILTER,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.EdgeFilter)
  })
_sym_db.RegisterMessage(EdgeFilter)

NeighborsRequest = _reflection.GeneratedProtocolMessageType('NeighborsRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBORSREQUEST,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.NeighborsRequest)
  })
_sym_db.RegisterMessage(NeighborsRequest)

NeighborsResponse = _reflection.GeneratedProtocolMessageType('NeighborsResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBORSRESPONSE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.NeighborsResponse)
  })
_sym_db.RegisterMessage(NeighborsResponse)

TraverseRequest = _reflection.GeneratedProtocolMessageType('TraverseRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAVERSEREQUEST,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.TraverseRequest)
  })
_sym_db.RegisterMessage(TraverseRequest)

TraverseResponse = _reflection.GeneratedProtocolMessageType('TraverseResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAVERSERESPONSE,
  '__module__' : 'graphstore.api.v1beta.graphstore_pb2'
  # @@protoc_insertion_point(class_scope:graphstore.api.v1beta.TraverseResponse)
  })
_sym_db.RegisterMessage(TraverseResponse)


DESCRIPTOR._options = None

_GRAPHSTORE = _descriptor.ServiceDescriptor(
  name='GraphStore',
  full_name='graphstore.api.v1beta.GraphStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1347,
  serialized_end=1798,
  methods=[
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='graphstore.api.v1beta.GraphStore.Put',
    index=0,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_PUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='graphstore.api.v1beta.GraphStore.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='graphstore.api.v1beta.GraphStore.List',
    index=2,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Neighbors',
    full_name='graphstore.api.v1beta.GraphStore.Neighbors',
    index=3,
    containing_service=None,
    input_type=_NEIGHBORSREQUEST,
    output_type=_NEIGHBORSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Traverse',
    full_name='graphstore.api.v1beta.GraphStore.Traverse',
    index=4,
    containing_service=None,
    input_type=_TRAVERSEREQUEST,
    output_type=_TRAVERSERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRAPHSTORE)

DESCRIPTOR.services_by_name['GraphStore'] = _GRAPHSTORE

# @@protoc_insertion_point(module_scope)
