# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: board.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import item_pb2 as item__pb2
import character_pb2 as character__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='board.proto',
  package='board',
  syntax='proto3',
  serialized_options=b'\n\036mech.mania.engine.domain.modelB\013BoardProtos\252\002\016MM26.IO.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x62oard.proto\x12\x05\x62oard\x1a\nitem.proto\x1a\x0f\x63haracter.proto\"g\n\x05\x42oard\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x19\n\x04grid\x18\x03 \x03(\x0b\x32\x0b.board.Tile\x12$\n\x07portals\x18\x04 \x03(\x0b\x32\x13.character.Position\"\xb4\x01\n\x04Tile\x12\'\n\ttile_type\x18\x01 \x01(\x0e\x32\x14.board.Tile.TileType\x12\x19\n\x05items\x18\x02 \x03(\x0b\x32\n.item.Item\x12\x15\n\rground_sprite\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x62ove_sprite\x18\x04 \x01(\t\";\n\x08TileType\x12\x08\n\x04VOID\x10\x00\x12\t\n\x05\x42LANK\x10\x01\x12\x0e\n\nIMPASSIBLE\x10\x02\x12\n\n\x06PORTAL\x10\x03\x42>\n\x1emech.mania.engine.domain.modelB\x0b\x42oardProtos\xaa\x02\x0eMM26.IO.Modelsb\x06proto3'
  ,
  dependencies=[item__pb2.DESCRIPTOR,character__pb2.DESCRIPTOR,])



_TILE_TILETYPE = _descriptor.EnumDescriptor(
  name='TileType',
  full_name='board.Tile.TileType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VOID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLANK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMPASSIBLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PORTAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=278,
  serialized_end=337,
)
_sym_db.RegisterEnumDescriptor(_TILE_TILETYPE)


_BOARD = _descriptor.Descriptor(
  name='Board',
  full_name='board.Board',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='board.Board.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='board.Board.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grid', full_name='board.Board.grid', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='portals', full_name='board.Board.portals', index=3,
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
  serialized_start=51,
  serialized_end=154,
)


_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='board.Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tile_type', full_name='board.Tile.tile_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='board.Tile.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ground_sprite', full_name='board.Tile.ground_sprite', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='above_sprite', full_name='board.Tile.above_sprite', index=3,
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
    _TILE_TILETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=337,
)

_BOARD.fields_by_name['grid'].message_type = _TILE
_BOARD.fields_by_name['portals'].message_type = character__pb2._POSITION
_TILE.fields_by_name['tile_type'].enum_type = _TILE_TILETYPE
_TILE.fields_by_name['items'].message_type = item__pb2._ITEM
_TILE_TILETYPE.containing_type = _TILE
DESCRIPTOR.message_types_by_name['Board'] = _BOARD
DESCRIPTOR.message_types_by_name['Tile'] = _TILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Board = _reflection.GeneratedProtocolMessageType('Board', (_message.Message,), {
  'DESCRIPTOR' : _BOARD,
  '__module__' : 'board_pb2'
  # @@protoc_insertion_point(class_scope:board.Board)
  })
_sym_db.RegisterMessage(Board)

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), {
  'DESCRIPTOR' : _TILE,
  '__module__' : 'board_pb2'
  # @@protoc_insertion_point(class_scope:board.Tile)
  })
_sym_db.RegisterMessage(Tile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
