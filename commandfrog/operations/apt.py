from commandfrog.drivers.driver import Driver
from typing import List


def init_apt(host: Driver):
    if host.exec("ls /var/lib/apt/lists/* > /dev/null", assert_ok=False).return_code != 0:
        apt_update(host)


def apt_update(host: Driver):
    host.exec("apt-get update -y", sudo=host.has_sudo)


def apt_install(host: Driver, packages: List[str]):
    installed_packages = host.exec("dpkg --get-selections |grep -v deinstall |cut -f 1").stdout.splitlines()
    packages_to_install = set(packages) - set(installed_packages)
    if packages_to_install:
        host.exec(f"apt-get install -y {' '.join(packages_to_install)}", sudo=host.has_sudo)

