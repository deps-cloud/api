# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depscloud/api/v1beta/core.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depscloud/api/v1beta/core.proto',
  package='depscloud.api.v1beta',
  syntax='proto3',
  serialized_options=b'Z\037github.com/depscloud/api/v1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x64\x65pscloud/api/v1beta/core.proto\x12\x14\x64\x65pscloud.api.v1beta\"N\n\x0bProviderURL\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x11\n\treference\x18\x04 \x01(\t\"\x8c\x01\n\x06Source\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x38\n\x06labels\x18\x05 \x03(\x0b\x32(.depscloud.api.v1beta.Source.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x01\n\x06Module\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x38\n\x06labels\x18\x05 \x03(\x0b\x32(.depscloud.api.v1beta.Module.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9e\x01\n\x0cSourceModule\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0e\n\x06system\x18\x02 \x01(\t\x12>\n\x06labels\x18\x05 \x03(\x0b\x32..depscloud.api.v1beta.SourceModule.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc2\x01\n\x10ModuleDependency\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1a\n\x12version_constraint\x18\x02 \x01(\t\x12\x0e\n\x06scopes\x18\x03 \x03(\t\x12\x42\n\x06labels\x18\x05 \x03(\x0b\x32\x32.depscloud.api.v1beta.ModuleDependency.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42!Z\x1fgithub.com/depscloud/api/v1betab\x06proto3'
)




_PROVIDERURL = _descriptor.Descriptor(
  name='ProviderURL',
  full_name='depscloud.api.v1beta.ProviderURL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='depscloud.api.v1beta.ProviderURL.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='depscloud.api.v1beta.ProviderURL.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='depscloud.api.v1beta.ProviderURL.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference', full_name='depscloud.api.v1beta.ProviderURL.reference', index=3,
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
  serialized_start=57,
  serialized_end=135,
)


_SOURCE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='depscloud.api.v1beta.Source.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='depscloud.api.v1beta.Source.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='depscloud.api.v1beta.Source.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=278,
)

_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='depscloud.api.v1beta.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='depscloud.api.v1beta.Source.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='depscloud.api.v1beta.Source.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='depscloud.api.v1beta.Source.labels', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SOURCE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=278,
)


_MODULE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='depscloud.api.v1beta.Module.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='depscloud.api.v1beta.Module.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='depscloud.api.v1beta.Module.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=278,
)

_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='depscloud.api.v1beta.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='depscloud.api.v1beta.Module.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='depscloud.api.v1beta.Module.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='depscloud.api.v1beta.Module.labels', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MODULE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=426,
)


_SOURCEMODULE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='depscloud.api.v1beta.SourceModule.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='depscloud.api.v1beta.SourceModule.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='depscloud.api.v1beta.SourceModule.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=278,
)

_SOURCEMODULE = _descriptor.Descriptor(
  name='SourceModule',
  full_name='depscloud.api.v1beta.SourceModule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='depscloud.api.v1beta.SourceModule.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system', full_name='depscloud.api.v1beta.SourceModule.system', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='depscloud.api.v1beta.SourceModule.labels', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SOURCEMODULE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=587,
)


_MODULEDEPENDENCY_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='depscloud.api.v1beta.ModuleDependency.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='depscloud.api.v1beta.ModuleDependency.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='depscloud.api.v1beta.ModuleDependency.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=278,
)

_MODULEDEPENDENCY = _descriptor.Descriptor(
  name='ModuleDependency',
  full_name='depscloud.api.v1beta.ModuleDependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='depscloud.api.v1beta.ModuleDependency.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_constraint', full_name='depscloud.api.v1beta.ModuleDependency.version_constraint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='depscloud.api.v1beta.ModuleDependency.scopes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='depscloud.api.v1beta.ModuleDependency.labels', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MODULEDEPENDENCY_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=784,
)

_SOURCE_LABELSENTRY.containing_type = _SOURCE
_SOURCE.fields_by_name['labels'].message_type = _SOURCE_LABELSENTRY
_MODULE_LABELSENTRY.containing_type = _MODULE
_MODULE.fields_by_name['labels'].message_type = _MODULE_LABELSENTRY
_SOURCEMODULE_LABELSENTRY.containing_type = _SOURCEMODULE
_SOURCEMODULE.fields_by_name['labels'].message_type = _SOURCEMODULE_LABELSENTRY
_MODULEDEPENDENCY_LABELSENTRY.containing_type = _MODULEDEPENDENCY
_MODULEDEPENDENCY.fields_by_name['labels'].message_type = _MODULEDEPENDENCY_LABELSENTRY
DESCRIPTOR.message_types_by_name['ProviderURL'] = _PROVIDERURL
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['SourceModule'] = _SOURCEMODULE
DESCRIPTOR.message_types_by_name['ModuleDependency'] = _MODULEDEPENDENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProviderURL = _reflection.GeneratedProtocolMessageType('ProviderURL', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDERURL,
  '__module__' : 'depscloud.api.v1beta.core_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ProviderURL)
  })
_sym_db.RegisterMessage(ProviderURL)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SOURCE_LABELSENTRY,
    '__module__' : 'depscloud.api.v1beta.core_pb2'
    # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.Source.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'depscloud.api.v1beta.core_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.Source)
  })
_sym_db.RegisterMessage(Source)
_sym_db.RegisterMessage(Source.LabelsEntry)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MODULE_LABELSENTRY,
    '__module__' : 'depscloud.api.v1beta.core_pb2'
    # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.Module.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'depscloud.api.v1beta.core_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.Module)
  })
_sym_db.RegisterMessage(Module)
_sym_db.RegisterMessage(Module.LabelsEntry)

SourceModule = _reflection.GeneratedProtocolMessageType('SourceModule', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SOURCEMODULE_LABELSENTRY,
    '__module__' : 'depscloud.api.v1beta.core_pb2'
    # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.SourceModule.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SOURCEMODULE,
  '__module__' : 'depscloud.api.v1beta.core_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.SourceModule)
  })
_sym_db.RegisterMessage(SourceModule)
_sym_db.RegisterMessage(SourceModule.LabelsEntry)

ModuleDependency = _reflection.GeneratedProtocolMessageType('ModuleDependency', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MODULEDEPENDENCY_LABELSENTRY,
    '__module__' : 'depscloud.api.v1beta.core_pb2'
    # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ModuleDependency.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _MODULEDEPENDENCY,
  '__module__' : 'depscloud.api.v1beta.core_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ModuleDependency)
  })
_sym_db.RegisterMessage(ModuleDependency)
_sym_db.RegisterMessage(ModuleDependency.LabelsEntry)


DESCRIPTOR._options = None
_SOURCE_LABELSENTRY._options = None
_MODULE_LABELSENTRY._options = None
_SOURCEMODULE_LABELSENTRY._options = None
_MODULEDEPENDENCY_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)