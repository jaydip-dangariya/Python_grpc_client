# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserService.proto',
  package='com.anand.grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11UserService.proto\x12\x0e\x63om.anand.grpc\"1\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07hobbies\x18\x03 \x03(\t\"_\n\x0e\x41\x64\x64UserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07hobbies\x18\x02 \x03(\t\x1a.\n\x08Response\x12\"\n\x04user\x18\x01 \x01(\x0b\x32\x14.com.anand.grpc.User\"h\n\x11GetAllUserRequest\x1aS\n\x08Response\x12#\n\x05users\x18\x01 \x03(\x0b\x32\x14.com.anand.grpc.User\x12\"\n\x04user\x18\x02 \x01(\x0b\x32\x14.com.anand.grpc.User2\xa7\x02\n\x0bUserService\x12R\n\x07\x61\x64\x64User\x12\x1e.com.anand.grpc.AddUserRequest\x1a\'.com.anand.grpc.AddUserRequest.Response\x12[\n\ngetAllUser\x12!.com.anand.grpc.GetAllUserRequest\x1a*.com.anand.grpc.GetAllUserRequest.Response\x12g\n\x14getAllUserWithStream\x12!.com.anand.grpc.GetAllUserRequest\x1a*.com.anand.grpc.GetAllUserRequest.Response0\x01\x62\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='com.anand.grpc.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.anand.grpc.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.anand.grpc.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hobbies', full_name='com.anand.grpc.User.hobbies', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=37,
  serialized_end=86,
)


_ADDUSERREQUEST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.anand.grpc.AddUserRequest.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='com.anand.grpc.AddUserRequest.Response.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=137,
  serialized_end=183,
)

_ADDUSERREQUEST = _descriptor.Descriptor(
  name='AddUserRequest',
  full_name='com.anand.grpc.AddUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.anand.grpc.AddUserRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hobbies', full_name='com.anand.grpc.AddUserRequest.hobbies', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ADDUSERREQUEST_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=183,
)


_GETALLUSERREQUEST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.anand.grpc.GetAllUserRequest.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='com.anand.grpc.GetAllUserRequest.Response.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='com.anand.grpc.GetAllUserRequest.Response.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=206,
  serialized_end=289,
)

_GETALLUSERREQUEST = _descriptor.Descriptor(
  name='GetAllUserRequest',
  full_name='com.anand.grpc.GetAllUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_GETALLUSERREQUEST_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=289,
)

_ADDUSERREQUEST_RESPONSE.fields_by_name['user'].message_type = _USER
_ADDUSERREQUEST_RESPONSE.containing_type = _ADDUSERREQUEST
_GETALLUSERREQUEST_RESPONSE.fields_by_name['users'].message_type = _USER
_GETALLUSERREQUEST_RESPONSE.fields_by_name['user'].message_type = _USER
_GETALLUSERREQUEST_RESPONSE.containing_type = _GETALLUSERREQUEST
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['AddUserRequest'] = _ADDUSERREQUEST
DESCRIPTOR.message_types_by_name['GetAllUserRequest'] = _GETALLUSERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'UserService_pb2'
  # @@protoc_insertion_point(class_scope:com.anand.grpc.User)
  ))
_sym_db.RegisterMessage(User)

AddUserRequest = _reflection.GeneratedProtocolMessageType('AddUserRequest', (_message.Message,), dict(

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _ADDUSERREQUEST_RESPONSE,
    __module__ = 'UserService_pb2'
    # @@protoc_insertion_point(class_scope:com.anand.grpc.AddUserRequest.Response)
    ))
  ,
  DESCRIPTOR = _ADDUSERREQUEST,
  __module__ = 'UserService_pb2'
  # @@protoc_insertion_point(class_scope:com.anand.grpc.AddUserRequest)
  ))
_sym_db.RegisterMessage(AddUserRequest)
_sym_db.RegisterMessage(AddUserRequest.Response)

GetAllUserRequest = _reflection.GeneratedProtocolMessageType('GetAllUserRequest', (_message.Message,), dict(

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _GETALLUSERREQUEST_RESPONSE,
    __module__ = 'UserService_pb2'
    # @@protoc_insertion_point(class_scope:com.anand.grpc.GetAllUserRequest.Response)
    ))
  ,
  DESCRIPTOR = _GETALLUSERREQUEST,
  __module__ = 'UserService_pb2'
  # @@protoc_insertion_point(class_scope:com.anand.grpc.GetAllUserRequest)
  ))
_sym_db.RegisterMessage(GetAllUserRequest)
_sym_db.RegisterMessage(GetAllUserRequest.Response)



_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='com.anand.grpc.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=292,
  serialized_end=587,
  methods=[
  _descriptor.MethodDescriptor(
    name='addUser',
    full_name='com.anand.grpc.UserService.addUser',
    index=0,
    containing_service=None,
    input_type=_ADDUSERREQUEST,
    output_type=_ADDUSERREQUEST_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getAllUser',
    full_name='com.anand.grpc.UserService.getAllUser',
    index=1,
    containing_service=None,
    input_type=_GETALLUSERREQUEST,
    output_type=_GETALLUSERREQUEST_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getAllUserWithStream',
    full_name='com.anand.grpc.UserService.getAllUserWithStream',
    index=2,
    containing_service=None,
    input_type=_GETALLUSERREQUEST,
    output_type=_GETALLUSERREQUEST_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)
