from paramiko import util as util
from paramiko.ber import BER as BER, BERException as BERException
from paramiko.common import zero_byte as zero_byte
from paramiko.message import Message as Message
from paramiko.pkey import PKey as PKey
from paramiko.ssh_exception import SSHException as SSHException
from typing import Any, Optional

class DSSKey(PKey):
    p: Any = ...
    q: Any = ...
    g: Any = ...
    y: Any = ...
    x: Any = ...
    public_blob: Any = ...
    size: Any = ...
    def __init__(self, msg: Optional[Any] = ..., data: Optional[Any] = ..., filename: Optional[Any] = ..., password: Optional[Any] = ..., vals: Optional[Any] = ..., file_obj: Optional[Any] = ...) -> None: ...
    def asbytes(self): ...
    def __hash__(self) -> Any: ...
    def get_name(self): ...
    def get_bits(self): ...
    def can_sign(self): ...
    def sign_ssh_data(self, data: Any): ...
    def verify_ssh_sig(self, data: Any, msg: Any): ...
    def write_private_key_file(self, filename: Any, password: Optional[Any] = ...) -> None: ...
    def write_private_key(self, file_obj: Any, password: Optional[Any] = ...) -> None: ...
    @staticmethod
    def generate(bits: int = ..., progress_func: Optional[Any] = ...): ...
