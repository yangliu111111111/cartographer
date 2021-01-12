# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/SubmapTexture.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class SubmapTexture(genpy.Message):
  _md5sum = "26187fc048d2d8e578b6c781f3b53158"
  _type = "cartographer_ros_msgs/SubmapTexture"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Copyright 2017 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

uint8[] cells
int32 width
int32 height
float64 resolution
geometry_msgs/Pose slice_pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['cells','width','height','resolution','slice_pose']
  _slot_types = ['uint8[]','int32','int32','float64','geometry_msgs/Pose']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cells,width,height,resolution,slice_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SubmapTexture, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cells is None:
        self.cells = b''
      if self.width is None:
        self.width = 0
      if self.height is None:
        self.height = 0
      if self.resolution is None:
        self.resolution = 0.
      if self.slice_pose is None:
        self.slice_pose = geometry_msgs.msg.Pose()
    else:
      self.cells = b''
      self.width = 0
      self.height = 0
      self.resolution = 0.
      self.slice_pose = geometry_msgs.msg.Pose()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.cells
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i8d().pack(_x.width, _x.height, _x.resolution, _x.slice_pose.position.x, _x.slice_pose.position.y, _x.slice_pose.position.z, _x.slice_pose.orientation.x, _x.slice_pose.orientation.y, _x.slice_pose.orientation.z, _x.slice_pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.slice_pose is None:
        self.slice_pose = geometry_msgs.msg.Pose()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cells = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.width, _x.height, _x.resolution, _x.slice_pose.position.x, _x.slice_pose.position.y, _x.slice_pose.position.z, _x.slice_pose.orientation.x, _x.slice_pose.orientation.y, _x.slice_pose.orientation.z, _x.slice_pose.orientation.w,) = _get_struct_2i8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.cells
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i8d().pack(_x.width, _x.height, _x.resolution, _x.slice_pose.position.x, _x.slice_pose.position.y, _x.slice_pose.position.z, _x.slice_pose.orientation.x, _x.slice_pose.orientation.y, _x.slice_pose.orientation.z, _x.slice_pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.slice_pose is None:
        self.slice_pose = geometry_msgs.msg.Pose()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cells = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.width, _x.height, _x.resolution, _x.slice_pose.position.x, _x.slice_pose.position.y, _x.slice_pose.position.z, _x.slice_pose.orientation.x, _x.slice_pose.orientation.y, _x.slice_pose.orientation.z, _x.slice_pose.orientation.w,) = _get_struct_2i8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i8d = None
def _get_struct_2i8d():
    global _struct_2i8d
    if _struct_2i8d is None:
        _struct_2i8d = struct.Struct("<2i8d")
    return _struct_2i8d
