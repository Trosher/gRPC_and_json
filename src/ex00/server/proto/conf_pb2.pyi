from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class eClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Corvette: _ClassVar[eClass]
    Frigate: _ClassVar[eClass]
    Cruiser: _ClassVar[eClass]
    Destroyer: _ClassVar[eClass]
    Carrier: _ClassVar[eClass]
    Dreadnought: _ClassVar[eClass]

class eAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Ally: _ClassVar[eAlignment]
    Enemy: _ClassVar[eAlignment]
Corvette: eClass
Frigate: eClass
Cruiser: eClass
Destroyer: eClass
Carrier: eClass
Dreadnought: eClass
Ally: eAlignment
Enemy: eAlignment

class cord(_message.Message):
    __slots__ = ("num0", "num1", "num2", "num3", "num4", "num5")
    NUM0_FIELD_NUMBER: _ClassVar[int]
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    NUM3_FIELD_NUMBER: _ClassVar[int]
    NUM4_FIELD_NUMBER: _ClassVar[int]
    NUM5_FIELD_NUMBER: _ClassVar[int]
    num0: float
    num1: float
    num2: float
    num3: float
    num4: float
    num5: float
    def __init__(self, num0: _Optional[float] = ..., num1: _Optional[float] = ..., num2: _Optional[float] = ..., num3: _Optional[float] = ..., num4: _Optional[float] = ..., num5: _Optional[float] = ...) -> None: ...

class Person(_message.Message):
    __slots__ = ("first_name", "last_name", "rank")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    rank: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...

class allShip(_message.Message):
    __slots__ = ("alignment", "name", "clas", "length", "crewSize", "armed", "officers")
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLAS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CREWSIZE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    OFFICERS_FIELD_NUMBER: _ClassVar[int]
    alignment: eAlignment
    name: str
    clas: eClass
    length: float
    crewSize: int
    armed: bool
    officers: _containers.RepeatedCompositeFieldContainer[Person]
    def __init__(self, alignment: _Optional[_Union[eAlignment, str]] = ..., name: _Optional[str] = ..., clas: _Optional[_Union[eClass, str]] = ..., length: _Optional[float] = ..., crewSize: _Optional[int] = ..., armed: bool = ..., officers: _Optional[_Iterable[_Union[Person, _Mapping]]] = ...) -> None: ...
