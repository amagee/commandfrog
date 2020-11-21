import importlib
import subprocess
import sys
from typing import Dict

import typer
from loguru import logger
import yaml

from infra.drivers.driver import Driver
from infra.drivers.ssh import SSHHost
from infra.drivers.local import LocalHost
from infra.drivers.docker import DockerHost



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

    module_name, func_name = deploy.rsplit(".", maxsplit=1)
    deploy_func = getattr(importlib.import_module(module_name), func_name)

    try:
        deploy_func(host_ob)
    finally:
        host_ob.disconnect()


if __name__ == "__main__":
    typer.run(main)
