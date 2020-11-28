import subprocess
from io import StringIO, BytesIO
import shlex
import tempfile
import os
from typing import Dict, Optional, Union

from loguru import logger

from commandfrog.config import Config
from commandfrog.drivers.driver import Driver, Result
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
            self.exec(f"chmod 600 {path}")

    def base_exec(self, cmd, assert_ok=True):
        cmd = f"docker exec {self.container_id} sh -c {shlex.quote(cmd)}",
        return execute_command(cmd, assert_ok=assert_ok)

    def commit(self):
        proc = subprocess.run(f"docker commit {self.container_id}", stdout=subprocess.PIPE, shell=True)
        new_image_id = proc.stdout.decode().strip().split(":")[1]
        print(f"New image id is {new_image_id}")

    def disconnect(self):
        self.commit()



