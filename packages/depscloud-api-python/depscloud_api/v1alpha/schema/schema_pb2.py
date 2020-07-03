# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depscloud_api/v1alpha/schema/schema.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depscloud_api/v1alpha/schema/schema.proto',
  package='cloud.deps.api.v1alpha.schema',
  syntax='proto3',
  serialized_options=b'Z\'github.com/depscloud/api/v1alpha/schema',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)depscloud_api/v1alpha/schema/schema.proto\x12\x1d\x63loud.deps.api.v1alpha.schema\"0\n\x06Source\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\"<\n\x07Manages\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0e\n\x06system\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"@\n\x06Module\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x14\n\x0corganization\x18\x02 \x01(\t\x12\x0e\n\x06module\x18\x03 \x01(\t\"T\n\x07\x44\x65pends\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x1a\n\x12version_constraint\x18\x02 \x01(\t\x12\x0e\n\x06scopes\x18\x03 \x03(\t\x12\x0b\n\x03ref\x18\x04 \x01(\tB)Z\'github.com/depscloud/api/v1alpha/schemab\x06proto3'
)




_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='cloud.deps.api.v1alpha.schema.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='cloud.deps.api.v1alpha.schema.Source.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ref', full_name='cloud.deps.api.v1alpha.schema.Source.ref', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='cloud.deps.api.v1alpha.schema.Source.kind', index=2,
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
  serialized_start=76,
  serialized_end=124,
)


_MANAGES = _descriptor.Descriptor(
  name='Manages',
  full_name='cloud.deps.api.v1alpha.schema.Manages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='cloud.deps.api.v1alpha.schema.Manages.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system', full_name='cloud.deps.api.v1alpha.schema.Manages.system', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='cloud.deps.api.v1alpha.schema.Manages.version', index=2,
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
  serialized_start=126,
  serialized_end=186,
)


_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='cloud.deps.api.v1alpha.schema.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='cloud.deps.api.v1alpha.schema.Module.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization', full_name='cloud.deps.api.v1alpha.schema.Module.organization', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='cloud.deps.api.v1alpha.schema.Module.module', index=2,
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
  serialized_start=188,
  serialized_end=252,
)


_DEPENDS = _descriptor.Descriptor(
  name='Depends',
  full_name='cloud.deps.api.v1alpha.schema.Depends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='cloud.deps.api.v1alpha.schema.Depends.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_constraint', full_name='cloud.deps.api.v1alpha.schema.Depends.version_constraint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='cloud.deps.api.v1alpha.schema.Depends.scopes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ref', full_name='cloud.deps.api.v1alpha.schema.Depends.ref', index=3,
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
  serialized_start=254,
  serialized_end=338,
)

DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['Manages'] = _MANAGES
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['Depends'] = _DEPENDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'depscloud_api.v1alpha.schema.schema_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.schema.Source)
  })
_sym_db.RegisterMessage(Source)

Manages = _reflection.GeneratedProtocolMessageType('Manages', (_message.Message,), {
  'DESCRIPTOR' : _MANAGES,
  '__module__' : 'depscloud_api.v1alpha.schema.schema_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.schema.Manages)
  })
_sym_db.RegisterMessage(Manages)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'depscloud_api.v1alpha.schema.schema_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.schema.Module)
  })
_sym_db.RegisterMessage(Module)

Depends = _reflection.GeneratedProtocolMessageType('Depends', (_message.Message,), {
  'DESCRIPTOR' : _DEPENDS,
  '__module__' : 'depscloud_api.v1alpha.schema.schema_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.schema.Depends)
  })
_sym_db.RegisterMessage(Depends)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
