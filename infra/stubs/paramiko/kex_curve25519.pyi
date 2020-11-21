from paramiko.message import Message as Message
from paramiko.py3compat import byte_chr as byte_chr, long as long
from paramiko.ssh_exception import SSHException as SSHException
from typing import Any

c_MSG_KEXECDH_INIT: Any
c_MSG_KEXECDH_REPLY: Any

class KexCurve25519:
    hash_algo: Any = ...
    transport: Any = ...
    key: Any = ...
    def __init__(self, transport: Any) -> None: ...
    @classmethod
    def is_available(cls): ...
    def start_kex(self) -> None: ...
    def parse_next(self, ptype: Any, m: Any): ...
