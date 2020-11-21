from paramiko import util as util
from paramiko.common import o600 as o600
from paramiko.message import Message as Message
from paramiko.py3compat import b as b, decodebytes as decodebytes, encodebytes as encodebytes, string_types as string_types, u as u
from paramiko.ssh_exception import PasswordRequiredException as PasswordRequiredException, SSHException as SSHException
from typing import Any, Optional

OPENSSH_AUTH_MAGIC: bytes

class PKey:
    BEGIN_TAG: Any = ...
    END_TAG: Any = ...
    def __init__(self, msg: Optional[Any] = ..., data: Optional[Any] = ...) -> None: ...
    def asbytes(self): ...
    def __cmp__(self, other: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def get_name(self): ...
    def get_bits(self): ...
    def can_sign(self): ...
    def get_fingerprint(self): ...
    def get_base64(self): ...
    def sign_ssh_data(self, data: Any): ...
    def verify_ssh_sig(self, data: Any, msg: Any): ...
    @classmethod
    def from_private_key_file(cls, filename: Any, password: Optional[Any] = ...): ...
    @classmethod
    def from_private_key(cls, file_obj: Any, password: Optional[Any] = ...): ...
    def write_private_key_file(self, filename: Any, password: Optional[Any] = ...) -> None: ...
    def write_private_key(self, file_obj: Any, password: Optional[Any] = ...) -> None: ...
    public_blob: Any = ...
    def load_certificate(self, value: Any) -> None: ...

class PublicBlob:
    key_type: Any = ...
    key_blob: Any = ...
    comment: Any = ...
    def __init__(self, type_: Any, blob: Any, comment: Optional[Any] = ...) -> None: ...
    @classmethod
    def from_file(cls, filename: Any): ...
    @classmethod
    def from_string(cls, string: Any): ...
    @classmethod
    def from_message(cls, message: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
