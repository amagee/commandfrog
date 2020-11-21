from infra.drivers.driver import Driver


def is_directory(host: Driver, path: str):
    return host.exec(f"test -d {path}", assert_ok=False).return_code == 0


def is_regular_file(host: Driver, path: str):
    return host.exec(f"test -f {path}", assert_ok=False).return_code == 0


def directory(host: Driver, path: str):
    if not is_directory(host, path):
        host.exec(f"mkdir -p {path}")



