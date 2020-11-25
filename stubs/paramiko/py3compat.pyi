import base64
import builtins as builtins
import io
from typing import Any

PY2: Any
string_types = str
text_type = str
bytes = bytes
bytes_types = bytes
integer_types = int

class long(int): ...
input = input
decodebytes = base64.decodebytes
encodebytes = base64.encodebytes

def byte_ord(c: Any): ...
def byte_chr(c: Any): ...
def byte_mask(c: Any, mask: Any): ...
def b(s: Any, encoding: str = ...): ...
def u(s: Any, encoding: str = ...): ...
def b2s(s: Any): ...
StringIO = io.StringIO
BytesIO = io.BytesIO

def is_callable(c: Any): ...
next = next
MAXSIZE: Any
