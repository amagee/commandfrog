import ctypes.wintypes
from paramiko.common import zero_byte as zero_byte
from paramiko.py3compat import b as b
from typing import Any

win32con_WM_COPYDATA: int

def can_talk_to_agent(): ...
ULONG_PTR = ctypes.c_uint64
ULONG_PTR = ctypes.c_uint32

class COPYDATASTRUCT(ctypes.Structure): ...

class PageantConnection:
    def __init__(self) -> None: ...
    def send(self, data: Any) -> None: ...
    def recv(self, n: Any): ...
    def close(self) -> None: ...
