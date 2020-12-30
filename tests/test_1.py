from pathlib import Path
import tempfile
import textwrap
from typing import cast

import docker
from docker.models.containers import Container

from commandfrog.run import main


def test_1():
    """
    Execute a simple deploy onto a docker container, and then check the
    committed image to make sure the deploy was executed correctly.
    """
    client = docker.from_env()
    container = cast(Container, client.containers.run("ubuntu", tty=True, command="/bin/bash", detach=True))
    new_image_id = None

    try:
        with tempfile.TemporaryDirectory() as dir:
            deploy_path = str(Path(dir) / "deploy.py")
            with open(deploy_path, "w+") as f:
                f.write(textwrap.dedent("""\
                    from commandfrog.drivers.driver import Driver

                    def mycommand(host: Driver):
                        host.exec("echo hello > ~/hello.txt")
                """))

            new_image_id = main(
                host=f"@docker/{container.id}",
                deploy=f"{deploy_path}:mycommand",
            )

            assert cast(bytes, client.containers.run(new_image_id, command=["cat", "/root/hello.txt"])).decode().strip() == "hello"
    finally:
        container.remove(force=True)
        client.images.remove(new_image_id, force=True)
