from getpass import getpass
from io import StringIO
import shlex
from typing import Optional, Union, Dict, List
from uuid import uuid4

from loguru import logger

from commandfrog.config import Config


class Driver:
    has_sudo = True
    config: Config
    env: Dict

    def __init__(self, config: Config):
        self.config = config
        self.env = {}

    def exec(
        self,
        cmd: str,
        sudo:bool = False,
        assert_ok: bool = True
    ) -> 'Result':
        logger.info("Executing command {}", cmd)
        if sudo:
            if self.config.ask_for_sudo_password:
                if "sudo_password" not in self.env:
                    sudo_password = getpass("sudo password: ")
                    self.env["sudo_password"] = sudo_password
                    self.put(
                        "/tmp/askpass", 
                        "\n".join([
                            "#!/bin/sh",
                            "echo $pwd"
                        ]),
                        mode=int("0700", 8)
                    )
                cmd = f"env pwd={self.env['sudo_password']} SUDO_ASKPASS=/tmp/askpass sudo -A sh -c {shlex.quote(cmd)}"
            else:
                cmd = "sudo " + cmd
        return self.base_exec(cmd, assert_ok=assert_ok)

    @property
    def home_dir(self) -> str:
        result = self.exec("eval echo ~`whoami`")
        return result.stdout.decode().strip()

    def commit(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def put(self, path: str, contents: Union[str, StringIO, bytes], mode: Optional[Union[str, int]] = None):
        raise NotImplemented

    def base_exec(self, cmd: str, assert_ok: bool = True) -> 'Result':
        raise NotImplemented

    def local(self, cmd):
        from .local import LocalHost
        LocalHost(config=self.config).exec(cmd)

    def exec_as_script(self, src: str):
        temp_file = f"/tmp/pyinfra-{uuid4()}"
        self.put(temp_file, StringIO(src))
        try:
            self.exec(f"chmod +x {temp_file}")
            self.exec(temp_file)
        finally:
            self.exec(f"rm {temp_file}")


class Result:
    def __init__(self, return_code: int, stdout: bytes, stderr: bytes):
        self.return_code = return_code
        self.stdout = stdout
        self.stderr = stderr



