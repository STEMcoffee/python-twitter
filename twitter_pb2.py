# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
_DEVICE = descriptor.EnumDescriptor(
  name='Device',
  full_name='twitter.Device',
  filename='Device',
  values=[
    descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SMS', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='IM', index=2, number=2,
      options=None,
      type=None),
  ],
  options=None,
)


NONE = 0
SMS = 1
IM = 2


_GEOCODE_UNIT = descriptor.EnumDescriptor(
  name='Unit',
  full_name='twitter.Geocode.Unit',
  filename='Unit',
  values=[
    descriptor.EnumValueDescriptor(
      name='MILES', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='KILOMETERS', index=1, number=1,
      options=None,
      type=None),
  ],
  options=None,
)


_USER_PROFILE = descriptor.Descriptor(
  name='Profile',
  full_name='twitter.User.Profile',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='image_url', full_name='twitter.User.Profile.image_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='background_color', full_name='twitter.User.Profile.background_color', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text_color', full_name='twitter.User.Profile.text_color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='link_color', full_name='twitter.User.Profile.link_color', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sidebar_fill_color', full_name='twitter.User.Profile.sidebar_fill_color', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sidebar_border_color', full_name='twitter.User.Profile.sidebar_border_color', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_USER = descriptor.Descriptor(
  name='User',
  full_name='twitter.User',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='twitter.User.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='twitter.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='screen_name', full_name='twitter.User.screen_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='location', full_name='twitter.User.location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='twitter.User.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='profile', full_name='twitter.User.profile', index=5,
      number=6, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='twitter.User.url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='protected', full_name='twitter.User.protected', index=7,
      number=8, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='followers_count', full_name='twitter.User.followers_count', index=8,
      number=9, type=13, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='friends_count', full_name='twitter.User.friends_count', index=9,
      number=10, type=13, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='created_at', full_name='twitter.User.created_at', index=10,
      number=11, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='favorites_count', full_name='twitter.User.favorites_count', index=11,
      number=12, type=13, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='utc_offset', full_name='twitter.User.utc_offset', index=12,
      number=13, type=17, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_zone', full_name='twitter.User.time_zone', index=13,
      number=14, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='following', full_name='twitter.User.following', index=14,
      number=15, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='notifications', full_name='twitter.User.notifications', index=15,
      number=16, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='statuses_count', full_name='twitter.User.statuses_count', index=16,
      number=17, type=13, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='twitter.User.status', index=17,
      number=18, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_STATUS = descriptor.Descriptor(
  name='Status',
  full_name='twitter.Status',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='created_at', full_name='twitter.Status.created_at', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='twitter.Status.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text', full_name='twitter.Status.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source', full_name='twitter.Status.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='truncated', full_name='twitter.Status.truncated', index=4,
      number=5, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='in_reply_to_status_id', full_name='twitter.Status.in_reply_to_status_id', index=5,
      number=6, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='in_reply_to_user_id', full_name='twitter.Status.in_reply_to_user_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='favorited', full_name='twitter.Status.favorited', index=7,
      number=8, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='twitter.Status.user', index=8,
      number=9, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_DIRECTMESSAGE = descriptor.Descriptor(
  name='DirectMessage',
  full_name='twitter.DirectMessage',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='twitter.DirectMessage.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text', full_name='twitter.DirectMessage.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender_id', full_name='twitter.DirectMessage.sender_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recipient_id', full_name='twitter.DirectMessage.recipient_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='created_at', full_name='twitter.DirectMessage.created_at', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender_screen_name', full_name='twitter.DirectMessage.sender_screen_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recipient_screen_name', full_name='twitter.DirectMessage.recipient_screen_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender', full_name='twitter.DirectMessage.sender', index=7,
      number=8, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recipient', full_name='twitter.DirectMessage.recipient', index=8,
      number=9, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_TRENDS_TREND = descriptor.Descriptor(
  name='Trend',
  full_name='twitter.Trends.Trend',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='twitter.Trends.Trend.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='twitter.Trends.Trend.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_TRENDS = descriptor.Descriptor(
  name='Trends',
  full_name='twitter.Trends',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='as_of', full_name='twitter.Trends.as_of', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trends', full_name='twitter.Trends.trends', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_RESULTS_RESULT = descriptor.Descriptor(
  name='Result',
  full_name='twitter.Results.Result',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='created_at', full_name='twitter.Results.Result.created_at', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='from_user', full_name='twitter.Results.Result.from_user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='from_user_id', full_name='twitter.Results.Result.from_user_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='twitter.Results.Result.id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='iso_language_code', full_name='twitter.Results.Result.iso_language_code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='profile_image_url', full_name='twitter.Results.Result.profile_image_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source', full_name='twitter.Results.Result.source', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text', full_name='twitter.Results.Result.text', index=7,
      number=8, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='to_user', full_name='twitter.Results.Result.to_user', index=8,
      number=9, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='to_user_id', full_name='twitter.Results.Result.to_user_id', index=9,
      number=10, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='results_per_page', full_name='twitter.Results.Result.results_per_page', index=10,
      number=11, type=17, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_RESULTS = descriptor.Descriptor(
  name='Results',
  full_name='twitter.Results',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='completed_in', full_name='twitter.Results.completed_in', index=0,
      number=1, type=1, cpp_type=5, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_id', full_name='twitter.Results.max_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_page', full_name='twitter.Results.next_page', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='page', full_name='twitter.Results.page', index=3,
      number=4, type=13, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='query', full_name='twitter.Results.query', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='refresh_url', full_name='twitter.Results.refresh_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='results', full_name='twitter.Results.results', index=6,
      number=7, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='since_id', full_name='twitter.Results.since_id', index=7,
      number=8, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_GEOCODE = descriptor.Descriptor(
  name='Geocode',
  full_name='twitter.Geocode',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='latitude', full_name='twitter.Geocode.latitude', index=0,
      number=1, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='longitude', full_name='twitter.Geocode.longitude', index=1,
      number=2, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='radius', full_name='twitter.Geocode.radius', index=2,
      number=3, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='unit', full_name='twitter.Geocode.unit', index=3,
      number=4, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _GEOCODE_UNIT,
  ],
  options=None)


_RATELIMITSTATUS = descriptor.Descriptor(
  name='RateLimitStatus',
  full_name='twitter.RateLimitStatus',
  filename='twitter.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hourly_limit', full_name='twitter.RateLimitStatus.hourly_limit', index=0,
      number=1, type=17, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reset_time', full_name='twitter.RateLimitStatus.reset_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reset_time_in_seconds', full_name='twitter.RateLimitStatus.reset_time_in_seconds', index=2,
      number=3, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='remaining_hits', full_name='twitter.RateLimitStatus.remaining_hits', index=3,
      number=4, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_USER.fields_by_name['profile'].message_type = _USER_PROFILE
_USER.fields_by_name['status'].message_type = _STATUS
_STATUS.fields_by_name['user'].message_type = _USER
_DIRECTMESSAGE.fields_by_name['sender'].message_type = _USER
_DIRECTMESSAGE.fields_by_name['recipient'].message_type = _USER
_TRENDS.fields_by_name['trends'].message_type = _TRENDS_TREND
_RESULTS.fields_by_name['results'].message_type = _RESULTS_RESULT
_GEOCODE.fields_by_name['unit'].enum_type = _GEOCODE_UNIT

class User(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Profile(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _USER_PROFILE
  DESCRIPTOR = _USER

class Status(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATUS

class DirectMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIRECTMESSAGE

class Trends(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Trend(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _TRENDS_TREND
  DESCRIPTOR = _TRENDS

class Results(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Result(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RESULTS_RESULT
  DESCRIPTOR = _RESULTS

class Geocode(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GEOCODE

class RateLimitStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RATELIMITSTATUS

