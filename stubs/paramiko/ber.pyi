from paramiko.common import max_byte as max_byte, zero_byte as zero_byte
from paramiko.py3compat import b as b, byte_chr as byte_chr, byte_ord as byte_ord, long as long
from typing import Any

class BERException(Exception): ...

class BER:
    content: Any = ...
    idx: int = ...
    def __init__(self, content: Any = ...) -> None: ...
    def asbytes(self): ...
    def decode(self): ...
    def decode_next(self): ...
    @staticmethod
    def decode_sequence(data: Any): ...
    def encode_tlv(self, ident: Any, val: Any) -> None: ...
    def encode(self, x: Any) -> None: ...
    @staticmethod
    def encode_sequence(data: Any): ...
