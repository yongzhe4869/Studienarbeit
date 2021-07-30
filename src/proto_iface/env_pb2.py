# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: env.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='env.proto',
  package='rlenv',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tenv.proto\x12\x05rlenv\"\x16\n\x05State\x12\r\n\x05value\x18\x01 \x03(\x01\"\x17\n\x06\x41\x63tion\x12\r\n\x05value\x18\x02 \x01(\x01\"\x9b\x01\n\x08\x45nvState\x12\x1b\n\x05state\x18\x03 \x01(\x0b\x32\x0c.rlenv.State\x12\x0e\n\x06reward\x18\x04 \x01(\x01\x12\x0c\n\x04\x64one\x18\x05 \x01(\x08\x12\'\n\x04info\x18\x06 \x03(\x0b\x32\x19.rlenv.EnvState.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)




_STATE = _descriptor.Descriptor(
  name='State',
  full_name='rlenv.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rlenv.State.value', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=20,
  serialized_end=42,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='rlenv.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rlenv.Action.value', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=44,
  serialized_end=67,
)


_ENVSTATE_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='rlenv.EnvState.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='rlenv.EnvState.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='rlenv.EnvState.InfoEntry.value', index=1,
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
  serialized_start=182,
  serialized_end=225,
)

_ENVSTATE = _descriptor.Descriptor(
  name='EnvState',
  full_name='rlenv.EnvState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='rlenv.EnvState.state', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward', full_name='rlenv.EnvState.reward', index=1,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done', full_name='rlenv.EnvState.done', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='rlenv.EnvState.info', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENVSTATE_INFOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=225,
)

_ENVSTATE_INFOENTRY.containing_type = _ENVSTATE
_ENVSTATE.fields_by_name['state'].message_type = _STATE
_ENVSTATE.fields_by_name['info'].message_type = _ENVSTATE_INFOENTRY
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['EnvState'] = _ENVSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'env_pb2'
  # @@protoc_insertion_point(class_scope:rlenv.State)
  })
_sym_db.RegisterMessage(State)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'env_pb2'
  # @@protoc_insertion_point(class_scope:rlenv.Action)
  })
_sym_db.RegisterMessage(Action)

EnvState = _reflection.GeneratedProtocolMessageType('EnvState', (_message.Message,), {

  'InfoEntry' : _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENVSTATE_INFOENTRY,
    '__module__' : 'env_pb2'
    # @@protoc_insertion_point(class_scope:rlenv.EnvState.InfoEntry)
    })
  ,
  'DESCRIPTOR' : _ENVSTATE,
  '__module__' : 'env_pb2'
  # @@protoc_insertion_point(class_scope:rlenv.EnvState)
  })
_sym_db.RegisterMessage(EnvState)
_sym_db.RegisterMessage(EnvState.InfoEntry)


_ENVSTATE_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)
