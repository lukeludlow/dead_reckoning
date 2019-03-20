# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ublox_msgs/CfgTMODE3.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CfgTMODE3(genpy.Message):
  _md5sum = "818be20c97f2b940a885faaabc0d98a1"
  _type = "ublox_msgs/CfgTMODE3"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# CFG-TMODE3 (0x06, 0x71)
# Time Mode Settings 3
#
# Configures the receiver to be in Time Mode. The position referred to in this
# message is that of the Antenna Reference Point (ARP). See the Time Mode 
# Description for details.
# 
# Supported on:
#  - u-blox 8 / u-blox M8 with protocol version 20 (only with High Precision
#    GNSS products)
#

uint8 CLASS_ID = 6
uint8 MESSAGE_ID = 113

uint8 version                     # Message version (0x00 for this version)
uint8 reserved1                   # Reserved

uint16 flags
uint16 FLAGS_MODE_MASK = 255      # Receiver Mode:
uint16 FLAGS_MODE_DISABLED = 0      # Disabled
uint16 FLAGS_MODE_SURVEY_IN = 1     # Survey In
uint16 FLAGS_MODE_FIXED = 2         # Fixed Mode (true ARP position required)
uint16 FLAGS_LLA = 256            # Position is given in LAT/LON/ALT 
                                  # (default is ECEF)

int32 ecefXOrLat                  # WGS84 ECEF X coordinate (or latitude) of
                                  # the ARP position, depending on flags above
                                  # [cm] or [deg / 1e-7]
int32 ecefYOrLon                  # WGS84 ECEF Y coordinate (or longitude) of
                                  # the ARP position, depending on flags above
                                  # [cm] or [deg / 1e-7]
int32 ecefZOrAlt                  # WGS84 ECEF Z coordinate (or altitude) of
                                  # the ARP position, depending on flags above
                                  # [cm]
int8 ecefXOrLatHP                 # High-precision WGS84 ECEF X coordinate (or
                                  # latitude) of the ARP position, depending on
                                  # flags above. Must be in the range -99..+99.
                                  # The precise WGS84 ECEF X coordinate in units
                                  # of cm, or the precise WGS84 ECEF latitude in
                                  # units of 1e-7 degrees, is given by
                                  # ecefXOrLat + (ecefXOrLatHP * 1e-2)
                                  # [0.1 mm] or [deg * 1e-9]
int8 ecefYOrLonHP                 # High-precision WGS84 ECEF Y coordinate (or
                                  # longitude) of the ARP position, depending on
                                  # flags above. Must be in the range -99..+99.
                                  # The precise WGS84 ECEF Y coordinate in units
                                  # of cm, or the precise WGS84 ECEF longitude 
                                  # in units of 1e-7 degrees, is given by
                                  # ecefYOrLon + (ecefYOrLonHP * 1e-2)
                                  # [0.1 mm] or [deg * 1e-9]
int8 ecefZOrAltHP                 # High-precision WGS84 ECEF Z coordinate (or
                                  # altitude) of the ARP position, depending on
                                  # flags above. Must be in the range -99..+99.
                                  # The precise WGS84 ECEF Z coordinate, or
                                  # altitude coordinate, in units of cm is given
                                  # by ecefZOrAlt + (ecefZOrAltHP * 1e-2)
                                  # [0.1 mm]
uint8 reserved2                   # Reserved

uint32 fixedPosAcc                # Fixed position 3D accuracy
                                  # [0.1 mm]
uint32 svinMinDur                 # Survey-in minimum duration
                                  # [s]
uint32 svinAccLimit               # Survey-in position accuracy limit
                                  # [0.1 mm]

uint8[8] reserved3                # Reserved
"""
  # Pseudo-constants
  CLASS_ID = 6
  MESSAGE_ID = 113
  FLAGS_MODE_MASK = 255
  FLAGS_MODE_DISABLED = 0
  FLAGS_MODE_SURVEY_IN = 1
  FLAGS_MODE_FIXED = 2
  FLAGS_LLA = 256

  __slots__ = ['version','reserved1','flags','ecefXOrLat','ecefYOrLon','ecefZOrAlt','ecefXOrLatHP','ecefYOrLonHP','ecefZOrAltHP','reserved2','fixedPosAcc','svinMinDur','svinAccLimit','reserved3']
  _slot_types = ['uint8','uint8','uint16','int32','int32','int32','int8','int8','int8','uint8','uint32','uint32','uint32','uint8[8]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       version,reserved1,flags,ecefXOrLat,ecefYOrLon,ecefZOrAlt,ecefXOrLatHP,ecefYOrLonHP,ecefZOrAltHP,reserved2,fixedPosAcc,svinMinDur,svinAccLimit,reserved3

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CfgTMODE3, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.version is None:
        self.version = 0
      if self.reserved1 is None:
        self.reserved1 = 0
      if self.flags is None:
        self.flags = 0
      if self.ecefXOrLat is None:
        self.ecefXOrLat = 0
      if self.ecefYOrLon is None:
        self.ecefYOrLon = 0
      if self.ecefZOrAlt is None:
        self.ecefZOrAlt = 0
      if self.ecefXOrLatHP is None:
        self.ecefXOrLatHP = 0
      if self.ecefYOrLonHP is None:
        self.ecefYOrLonHP = 0
      if self.ecefZOrAltHP is None:
        self.ecefZOrAltHP = 0
      if self.reserved2 is None:
        self.reserved2 = 0
      if self.fixedPosAcc is None:
        self.fixedPosAcc = 0
      if self.svinMinDur is None:
        self.svinMinDur = 0
      if self.svinAccLimit is None:
        self.svinAccLimit = 0
      if self.reserved3 is None:
        self.reserved3 = b'\0'*8
    else:
      self.version = 0
      self.reserved1 = 0
      self.flags = 0
      self.ecefXOrLat = 0
      self.ecefYOrLon = 0
      self.ecefZOrAlt = 0
      self.ecefXOrLatHP = 0
      self.ecefYOrLonHP = 0
      self.ecefZOrAltHP = 0
      self.reserved2 = 0
      self.fixedPosAcc = 0
      self.svinMinDur = 0
      self.svinAccLimit = 0
      self.reserved3 = b'\0'*8

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
      _x = self
      buff.write(_get_struct_2BH3i3bB3I().pack(_x.version, _x.reserved1, _x.flags, _x.ecefXOrLat, _x.ecefYOrLon, _x.ecefZOrAlt, _x.ecefXOrLatHP, _x.ecefYOrLonHP, _x.ecefZOrAltHP, _x.reserved2, _x.fixedPosAcc, _x.svinMinDur, _x.svinAccLimit))
      _x = self.reserved3
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_8B().pack(*_x))
      else:
        buff.write(_get_struct_8s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.version, _x.reserved1, _x.flags, _x.ecefXOrLat, _x.ecefYOrLon, _x.ecefZOrAlt, _x.ecefXOrLatHP, _x.ecefYOrLonHP, _x.ecefZOrAltHP, _x.reserved2, _x.fixedPosAcc, _x.svinMinDur, _x.svinAccLimit,) = _get_struct_2BH3i3bB3I().unpack(str[start:end])
      start = end
      end += 8
      self.reserved3 = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2BH3i3bB3I().pack(_x.version, _x.reserved1, _x.flags, _x.ecefXOrLat, _x.ecefYOrLon, _x.ecefZOrAlt, _x.ecefXOrLatHP, _x.ecefYOrLonHP, _x.ecefZOrAltHP, _x.reserved2, _x.fixedPosAcc, _x.svinMinDur, _x.svinAccLimit))
      _x = self.reserved3
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_8B().pack(*_x))
      else:
        buff.write(_get_struct_8s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.version, _x.reserved1, _x.flags, _x.ecefXOrLat, _x.ecefYOrLon, _x.ecefZOrAlt, _x.ecefXOrLatHP, _x.ecefYOrLonHP, _x.ecefZOrAltHP, _x.reserved2, _x.fixedPosAcc, _x.svinMinDur, _x.svinAccLimit,) = _get_struct_2BH3i3bB3I().unpack(str[start:end])
      start = end
      end += 8
      self.reserved3 = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8B = None
def _get_struct_8B():
    global _struct_8B
    if _struct_8B is None:
        _struct_8B = struct.Struct("<8B")
    return _struct_8B
_struct_2BH3i3bB3I = None
def _get_struct_2BH3i3bB3I():
    global _struct_2BH3i3bB3I
    if _struct_2BH3i3bB3I is None:
        _struct_2BH3i3bB3I = struct.Struct("<2BH3i3bB3I")
    return _struct_2BH3i3bB3I
_struct_8s = None
def _get_struct_8s():
    global _struct_8s
    if _struct_8s is None:
        _struct_8s = struct.Struct("<8s")
    return _struct_8s
