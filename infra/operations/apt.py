from infra.drivers.driver import Driver
from typing import List


def init_apt(host: Driver):
    if host.exec("ls /var/lib/apt/lists/* > /dev/null", assert_ok=False).return_code != 0:
        apt_update(host)


def apt_update(host: Driver):
    host.exec("apt-get update -y", sudo=host.has_sudo)


def apt_install(host: Driver, packages: List[str]):
    host.exec(f"apt-get install -y {' '.join(packages)}", sudo=host.has_sudo)



