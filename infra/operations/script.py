from infra.drivers.driver import Driver

from io import StringIO
from uuid import uuid4


def script_from_string(host: Driver, src: str) -> str:
    temp_file = f"/tmp/pyinfra-{uuid4()}"
    host.put(temp_file, StringIO(src))
    host.exec(f"chmod +x {temp_file}")
    return temp_file




