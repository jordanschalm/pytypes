Int = lambda x: type(x) == int
Float = lambda x: type(x) == float
Long = lambda x: type(x) == long
Complex = lambda x: type(x) == complex

Str = lambda x: type(x) == str
Unicode = lambda x: type(x) == unicode

List = lambda x: type(x) == list
Tuple = lambda x: type(x) == tuple

ByteArray = lambda x: type(x) == bytearray
Buffer = lambda x: type(x) == buffer
XRange = lambda x: type(x) == xrange

Set = lambda x: type(x) == set
FrozenSet = lambda x: type(x) == frozenset

Dict = lambda x: type(x) == dict
File = lambda x: type(x) == file
Function = lambda x: type(x) == callable(x)
Null = lambda x: x is None
Bool = lambda x: type(x) == bool

Any = lambda x: True


def ListOf(tp):
    def Is(val):
        return List(val) and all(map(tp, val))
    return Is

def TupleOf(tp):
    def Is(val):
        return Tuple(val) and all(map(tp, val))
    return Is

def SetOf(tp):
    def Is(val):
        return Set(val) and all(map(tp, val))
    return Is

def FrozenSetOf(tp):
    def Is(val):
        return FrozenSet(val) and all(map(tp, val))
    return Is

def DictOf(key_type, val_type):
    def Is(val):
        return Dict(val) and \
            all(map(key_type, val.keys())) and \
            all(map(val_type, val.values()))
    return Is
