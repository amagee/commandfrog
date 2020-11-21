from paramiko import util as util
from paramiko.common import DEBUG as DEBUG, asbytes as asbytes
from paramiko.message import Message as Message
from paramiko.py3compat import byte_chr as byte_chr, byte_ord as byte_ord
from typing import Any

CMD_INIT: Any
CMD_VERSION: Any
CMD_OPEN: Any
CMD_CLOSE: Any
CMD_READ: Any
CMD_WRITE: Any
CMD_LSTAT: Any
CMD_FSTAT: Any
CMD_SETSTAT: Any
CMD_FSETSTAT: Any
CMD_OPENDIR: Any
CMD_READDIR: Any
CMD_REMOVE: Any
CMD_MKDIR: Any
CMD_RMDIR: Any
CMD_REALPATH: Any
CMD_STAT: Any
CMD_RENAME: Any
CMD_READLINK: Any
CMD_SYMLINK: Any
CMD_STATUS: Any
CMD_HANDLE: Any
CMD_DATA: Any
CMD_NAME: Any
CMD_ATTRS: Any
CMD_EXTENDED: Any
CMD_EXTENDED_REPLY: Any
SFTP_OK: int
SFTP_EOF: Any
SFTP_NO_SUCH_FILE: Any
SFTP_PERMISSION_DENIED: Any
SFTP_FAILURE: Any
SFTP_BAD_MESSAGE: Any
SFTP_NO_CONNECTION: Any
SFTP_CONNECTION_LOST: Any
SFTP_OP_UNSUPPORTED: Any
SFTP_DESC: Any
SFTP_FLAG_READ: int
SFTP_FLAG_WRITE: int
SFTP_FLAG_APPEND: int
SFTP_FLAG_CREATE: int
SFTP_FLAG_TRUNC: int
SFTP_FLAG_EXCL: int
CMD_NAMES: Any

class SFTPError(Exception): ...

class BaseSFTP:
    logger: Any = ...
    sock: Any = ...
    ultra_debug: bool = ...
    def __init__(self) -> None: ...
