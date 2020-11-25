import importlib
import os
import subprocess
import sys
from typing import Dict

import typer
from loguru import logger
import yaml

from commandfrog.drivers.driver import Driver
from commandfrog.drivers.ssh import SSHHost
from commandfrog.drivers.local import LocalHost
from commandfrog.drivers.docker import DockerHost



def main(host: str, deploy: str, config: str = None):
    logger.remove()
    logger.add(
        sys.stderr,
        level="INFO",
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"
    )

    host_ob: Driver
    config_ob: Dict

    if config is not None:
        if config.lower().endswith((".yaml", ".yml")):
            config_ob = yaml.safe_load(open(config).read())
        else:
            raise ValueError("We only support yaml config")
    else:
        config_ob = {}

    if host == "@local":
        host_ob = LocalHost(config=config_ob)
    elif host.startswith("@docker/"):
        docker_item_id = host[len("@docker/"):]
        if subprocess.run(f"docker image inspect {docker_item_id} > /dev/null", shell=True).returncode == 0:
            host_ob = DockerHost(image_id=docker_item_id, config=config_ob)
        elif subprocess.run(f"docker container inspect {docker_item_id} > /dev/null", shell=True).returncode == 0:
            host_ob = DockerHost(container_id=docker_item_id, config=config_ob)
        else:
            raise ValueError("not image or container")
    else:
        username, hostname = host.split("@", maxsplit=1)
        host_ob = SSHHost(hostname=hostname, username=username, config=config_ob)

    # Don't assume the caller has a real Python environment setup (they may be calling
    # from the PyInstaller package), so support an arbitrary path to a Python file rather
    # than a regular Python import path.
    path, func_name = deploy.split(":")
    sys.path.insert(0, os.path.dirname(path))
    # For PyInstaller
    sys.path.append(os.path.dirname(sys.executable))
    module = importlib.import_module(os.path.basename(path.rstrip(".py")))
    deploy_func  = getattr(module, func_name)

    try:
        deploy_func(host_ob)
    finally:
        host_ob.disconnect()


if __name__ == "__main__":
    typer.run(main)
