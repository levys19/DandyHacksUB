# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision_v1/proto/web_detection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/vision_v1/proto/web_detection.proto',
  package='google.cloud.vision.v1',
  syntax='proto3',
  serialized_pb=_b('\n0google/cloud/vision_v1/proto/web_detection.proto\x12\x16google.cloud.vision.v1\x1a\x1cgoogle/api/annotations.proto\"\xd6\x03\n\x0cWebDetection\x12\x44\n\x0cweb_entities\x18\x01 \x03(\x0b\x32..google.cloud.vision.v1.WebDetection.WebEntity\x12K\n\x14\x66ull_matching_images\x18\x02 \x03(\x0b\x32-.google.cloud.vision.v1.WebDetection.WebImage\x12N\n\x17partial_matching_images\x18\x03 \x03(\x0b\x32-.google.cloud.vision.v1.WebDetection.WebImage\x12P\n\x1apages_with_matching_images\x18\x04 \x03(\x0b\x32,.google.cloud.vision.v1.WebDetection.WebPage\x1a\x42\n\tWebEntity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x1a&\n\x08WebImage\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x1a%\n\x07WebPage\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x42r\n\x1a\x63om.google.cloud.vision.v1B\x11WebDetectionProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/vision/v1;vision\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WEBDETECTION_WEBENTITY = _descriptor.Descriptor(
  name='WebEntity',
  full_name='google.cloud.vision.v1.WebDetection.WebEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='google.cloud.vision.v1.WebDetection.WebEntity.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='google.cloud.vision.v1.WebDetection.WebEntity.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.vision.v1.WebDetection.WebEntity.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=498,
)

_WEBDETECTION_WEBIMAGE = _descriptor.Descriptor(
  name='WebImage',
  full_name='google.cloud.vision.v1.WebDetection.WebImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.cloud.vision.v1.WebDetection.WebImage.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='google.cloud.vision.v1.WebDetection.WebImage.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=538,
)

_WEBDETECTION_WEBPAGE = _descriptor.Descriptor(
  name='WebPage',
  full_name='google.cloud.vision.v1.WebDetection.WebPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.cloud.vision.v1.WebDetection.WebPage.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='google.cloud.vision.v1.WebDetection.WebPage.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=540,
  serialized_end=577,
)

_WEBDETECTION = _descriptor.Descriptor(
  name='WebDetection',
  full_name='google.cloud.vision.v1.WebDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='web_entities', full_name='google.cloud.vision.v1.WebDetection.web_entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_matching_images', full_name='google.cloud.vision.v1.WebDetection.full_matching_images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partial_matching_images', full_name='google.cloud.vision.v1.WebDetection.partial_matching_images', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pages_with_matching_images', full_name='google.cloud.vision.v1.WebDetection.pages_with_matching_images', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WEBDETECTION_WEBENTITY, _WEBDETECTION_WEBIMAGE, _WEBDETECTION_WEBPAGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=577,
)

_WEBDETECTION_WEBENTITY.containing_type = _WEBDETECTION
_WEBDETECTION_WEBIMAGE.containing_type = _WEBDETECTION
_WEBDETECTION_WEBPAGE.containing_type = _WEBDETECTION
_WEBDETECTION.fields_by_name['web_entities'].message_type = _WEBDETECTION_WEBENTITY
_WEBDETECTION.fields_by_name['full_matching_images'].message_type = _WEBDETECTION_WEBIMAGE
_WEBDETECTION.fields_by_name['partial_matching_images'].message_type = _WEBDETECTION_WEBIMAGE
_WEBDETECTION.fields_by_name['pages_with_matching_images'].message_type = _WEBDETECTION_WEBPAGE
DESCRIPTOR.message_types_by_name['WebDetection'] = _WEBDETECTION

WebDetection = _reflection.GeneratedProtocolMessageType('WebDetection', (_message.Message,), dict(

  WebEntity = _reflection.GeneratedProtocolMessageType('WebEntity', (_message.Message,), dict(
    DESCRIPTOR = _WEBDETECTION_WEBENTITY,
    __module__ = 'google.cloud.vision_v1.proto.web_detection_pb2'
    ,
    __doc__ = """Entity deduced from similar images on the Internet.
    
    
    Attributes:
        entity_id:
            Opaque entity ID.
        score:
            Overall relevancy score for the entity. Not normalized and not
            comparable across different image queries.
        description:
            Canonical description of the entity, in English.
    """,
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.WebDetection.WebEntity)
    ))
  ,

  WebImage = _reflection.GeneratedProtocolMessageType('WebImage', (_message.Message,), dict(
    DESCRIPTOR = _WEBDETECTION_WEBIMAGE,
    __module__ = 'google.cloud.vision_v1.proto.web_detection_pb2'
    ,
    __doc__ = """Metadata for online images.
    
    
    Attributes:
        url:
            The result image URL.
        score:
            Overall relevancy score for the image. Not normalized and not
            comparable across different image queries.
    """,
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.WebDetection.WebImage)
    ))
  ,

  WebPage = _reflection.GeneratedProtocolMessageType('WebPage', (_message.Message,), dict(
    DESCRIPTOR = _WEBDETECTION_WEBPAGE,
    __module__ = 'google.cloud.vision_v1.proto.web_detection_pb2'
    ,
    __doc__ = """Metadata for web pages.
    
    
    Attributes:
        url:
            The result web page URL.
        score:
            Overall relevancy score for the web page. Not normalized and
            not comparable across different image queries.
    """,
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.WebDetection.WebPage)
    ))
  ,
  DESCRIPTOR = _WEBDETECTION,
  __module__ = 'google.cloud.vision_v1.proto.web_detection_pb2'
  ,
  __doc__ = """Relevant information for the image from the Internet.
  
  
  Attributes:
      web_entities:
          Deduced entities from similar images on the Internet.
      full_matching_images:
          Fully matching images from the Internet. They're definite
          neardups and most often a copy of the query image with merely
          a size change.
      partial_matching_images:
          Partial matching images from the Internet. Those images are
          similar enough to share some key-point features. For example
          an original image will likely have partial matching for its
          crops.
      pages_with_matching_images:
          Web pages containing the matching images from the Internet.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.WebDetection)
  ))
_sym_db.RegisterMessage(WebDetection)
_sym_db.RegisterMessage(WebDetection.WebEntity)
_sym_db.RegisterMessage(WebDetection.WebImage)
_sym_db.RegisterMessage(WebDetection.WebPage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.google.cloud.vision.v1B\021WebDetectionProtoP\001Z<google.golang.org/genproto/googleapis/cloud/vision/v1;vision\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
