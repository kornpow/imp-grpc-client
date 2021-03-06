# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: websocket.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='websocket.proto',
  package='websocket',
  syntax='proto3',
  serialized_options=b'Z#github.com/imperviousai/freeimp/gen\222A\240\001\022A\n\022Websocket Services\"&\n\rImpervious AI\022\025https://impervious.ai2\0031.0*\003\001\002\0042\020application/json:\020application/jsonr2\n\024Documentation on IMP\022\032https://docs.impervious.ai',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fwebsocket.proto\x12\twebsocket\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x12\n\x10SubscribeRequest\"}\n\x11SubscribeResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0breply_to_id\x18\x02 \x01(\t\x12\x13\n\x0b\x66rom_pubkey\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x14\n\x0cservice_type\x18\x05 \x01(\t\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x03\x32l\n\tWebsocket\x12_\n\tSubscribe\x12\x1b.websocket.SubscribeRequest\x1a\x1c.websocket.SubscribeResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/subscribe0\x01\x42\xc9\x01Z#github.com/imperviousai/freeimp/gen\x92\x41\xa0\x01\x12\x41\n\x12Websocket Services\"&\n\rImpervious AI\x12\x15https://impervious.ai2\x03\x31.0*\x03\x01\x02\x04\x32\x10\x61pplication/json:\x10\x61pplication/jsonr2\n\x14\x44ocumentation on IMP\x12\x1ahttps://docs.impervious.aib\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR,])




_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='websocket.SubscribeRequest',
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
  serialized_start=108,
  serialized_end=126,
)


_SUBSCRIBERESPONSE = _descriptor.Descriptor(
  name='SubscribeResponse',
  full_name='websocket.SubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='websocket.SubscribeResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to_id', full_name='websocket.SubscribeResponse.reply_to_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_pubkey', full_name='websocket.SubscribeResponse.from_pubkey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='websocket.SubscribeResponse.data', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_type', full_name='websocket.SubscribeResponse.service_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='websocket.SubscribeResponse.amount', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=128,
  serialized_end=253,
)

DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeResponse'] = _SUBSCRIBERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'websocket_pb2'
  # @@protoc_insertion_point(class_scope:websocket.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeResponse = _reflection.GeneratedProtocolMessageType('SubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERESPONSE,
  '__module__' : 'websocket_pb2'
  # @@protoc_insertion_point(class_scope:websocket.SubscribeResponse)
  })
_sym_db.RegisterMessage(SubscribeResponse)


DESCRIPTOR._options = None

_WEBSOCKET = _descriptor.ServiceDescriptor(
  name='Websocket',
  full_name='websocket.Websocket',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=255,
  serialized_end=363,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='websocket.Websocket.Subscribe',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIBERESPONSE,
    serialized_options=b'\202\323\344\223\002\017\022\r/v1/subscribe',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WEBSOCKET)

DESCRIPTOR.services_by_name['Websocket'] = _WEBSOCKET

# @@protoc_insertion_point(module_scope)
