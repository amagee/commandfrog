from paramiko.common import AUTH_FAILED as AUTH_FAILED, AUTH_PARTIALLY_SUCCESSFUL as AUTH_PARTIALLY_SUCCESSFUL, AUTH_SUCCESSFUL as AUTH_SUCCESSFUL, DEBUG as DEBUG, DISCONNECT_NO_MORE_AUTH_METHODS_AVAILABLE as DISCONNECT_NO_MORE_AUTH_METHODS_AVAILABLE, DISCONNECT_SERVICE_NOT_AVAILABLE as DISCONNECT_SERVICE_NOT_AVAILABLE, INFO as INFO, MSG_NAMES as MSG_NAMES, MSG_SERVICE_ACCEPT as MSG_SERVICE_ACCEPT, MSG_SERVICE_REQUEST as MSG_SERVICE_REQUEST, MSG_USERAUTH_BANNER as MSG_USERAUTH_BANNER, MSG_USERAUTH_FAILURE as MSG_USERAUTH_FAILURE, MSG_USERAUTH_GSSAPI_ERROR as MSG_USERAUTH_GSSAPI_ERROR, MSG_USERAUTH_GSSAPI_ERRTOK as MSG_USERAUTH_GSSAPI_ERRTOK, MSG_USERAUTH_GSSAPI_MIC as MSG_USERAUTH_GSSAPI_MIC, MSG_USERAUTH_GSSAPI_RESPONSE as MSG_USERAUTH_GSSAPI_RESPONSE, MSG_USERAUTH_GSSAPI_TOKEN as MSG_USERAUTH_GSSAPI_TOKEN, MSG_USERAUTH_INFO_REQUEST as MSG_USERAUTH_INFO_REQUEST, MSG_USERAUTH_INFO_RESPONSE as MSG_USERAUTH_INFO_RESPONSE, MSG_USERAUTH_REQUEST as MSG_USERAUTH_REQUEST, MSG_USERAUTH_SUCCESS as MSG_USERAUTH_SUCCESS, WARNING as WARNING, cMSG_DISCONNECT as cMSG_DISCONNECT, cMSG_SERVICE_ACCEPT as cMSG_SERVICE_ACCEPT, cMSG_SERVICE_REQUEST as cMSG_SERVICE_REQUEST, cMSG_USERAUTH_BANNER as cMSG_USERAUTH_BANNER, cMSG_USERAUTH_FAILURE as cMSG_USERAUTH_FAILURE, cMSG_USERAUTH_GSSAPI_MIC as cMSG_USERAUTH_GSSAPI_MIC, cMSG_USERAUTH_GSSAPI_RESPONSE as cMSG_USERAUTH_GSSAPI_RESPONSE, cMSG_USERAUTH_GSSAPI_TOKEN as cMSG_USERAUTH_GSSAPI_TOKEN, cMSG_USERAUTH_INFO_REQUEST as cMSG_USERAUTH_INFO_REQUEST, cMSG_USERAUTH_INFO_RESPONSE as cMSG_USERAUTH_INFO_RESPONSE, cMSG_USERAUTH_PK_OK as cMSG_USERAUTH_PK_OK, cMSG_USERAUTH_REQUEST as cMSG_USERAUTH_REQUEST, cMSG_USERAUTH_SUCCESS as cMSG_USERAUTH_SUCCESS
from paramiko.message import Message as Message
from paramiko.py3compat import b as b
from paramiko.server import InteractiveQuery as InteractiveQuery
from paramiko.ssh_exception import AuthenticationException as AuthenticationException, BadAuthenticationType as BadAuthenticationType, PartialAuthentication as PartialAuthentication, SSHException as SSHException
from paramiko.ssh_gss import GSSAuth as GSSAuth, GSS_EXCEPTIONS as GSS_EXCEPTIONS
from typing import Any

class AuthHandler:
    transport: Any = ...
    username: Any = ...
    authenticated: bool = ...
    auth_event: Any = ...
    auth_method: str = ...
    banner: Any = ...
    password: Any = ...
    private_key: Any = ...
    interactive_handler: Any = ...
    submethods: Any = ...
    auth_username: Any = ...
    auth_fail_count: int = ...
    gss_host: Any = ...
    gss_deleg_creds: bool = ...
    def __init__(self, transport: Any) -> None: ...
    def is_authenticated(self): ...
    def get_username(self): ...
    def auth_none(self, username: Any, event: Any) -> None: ...
    def auth_publickey(self, username: Any, key: Any, event: Any) -> None: ...
    def auth_password(self, username: Any, password: Any, event: Any) -> None: ...
    def auth_interactive(self, username: Any, handler: Any, event: Any, submethods: str = ...) -> None: ...
    def auth_gssapi_with_mic(self, username: Any, gss_host: Any, gss_deleg_creds: Any, event: Any) -> None: ...
    def auth_gssapi_keyex(self, username: Any, event: Any) -> None: ...
    def abort(self) -> None: ...
    def wait_for_response(self, event: Any): ...

class GssapiWithMicAuthHandler:
    method: str = ...
    sshgss: Any = ...
    def __init__(self, delegate: Any, sshgss: Any) -> None: ...
    def abort(self): ...
    @property
    def transport(self): ...
    @property
    def auth_username(self): ...
    @property
    def gss_host(self): ...
