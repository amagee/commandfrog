from io import StringIO
import os
import shlex
import subprocess
import tempfile
from typing import Optional, Union

from loguru import logger

from commandfrog.config import Config
from commandfrog.drivers.driver import Driver
from commandfrog.operations.files import directory

from .util import execute_command


class DockerHost(Driver):
    has_sudo = False

    container_id: Optional[str]

    def __init__(self, config: Config, image_id: Optional[str] = None, container_id: Optional[str] = None):
        super().__init__(config=config)

        self.image_id = image_id

        assert (image_id is not None) ^ (container_id is not None)

        if image_id is not None:
            self.container_id = subprocess.run(
                f'docker run -d {image_id} tail -f /dev/null',
                shell=True,
                stdout=subprocess.PIPE
            ).stdout.decode().splitlines()[-1]
        else:
            self.container_id = container_id

    def put(self, path: str, contents: Union[str, bytes, StringIO], mode: Optional[Union[str, int]] = None):
        directory(self, os.path.dirname(path))
        with tempfile.NamedTemporaryFile() as fp:
            if isinstance(contents, str):
                bytes = contents.encode()
            elif isinstance(contents, StringIO):
                bytes = contents.getvalue().encode()
            else:
                bytes = contents
            fp.write(bytes)
            fp.seek(0)
            cmd = f"docker cp {fp.name} {self.container_id}:{path}"
            logger.debug("Executing command: {}", cmd)
            subprocess.run(cmd, shell=True, check=True)
            self.exec(f"chmod {mode} {path}")

    def base_exec(self, cmd: str, assert_ok: bool = True):
        if self.container_id is None:
            raise ValueError("...")
        cmd = f"docker exec {self.container_id} sh -c {shlex.quote(cmd)}"
        return execute_command(cmd, assert_ok=assert_ok)

    def commit(self) -> str:
        """
        Run `docker commit`, return the new image ID.
        """
        proc = subprocess.run(f"docker commit {self.container_id}", stdout=subprocess.PIPE, shell=True)
        return proc.stdout.decode().strip().split(":")[1]

    def disconnect(self) -> str:
        return self.commit()



