import subprocess
from pathlib import Path
from functools import reduce
import operator


def build():
    subprocess.run("rm -rf dist", cwd="commandfrog", check=True, shell=True)

    operations = [p.stem for p in (Path("commandfrog") / "operations").glob("*.py")]

    # This creates a binary in `commandfrog/dist/run`.
    subprocess.run(
        [
            "pyinstaller",
            *reduce(
                operator.iconcat,
                [["--hidden-import", f"commandfrog.operations.{f}"] for f in operations]
            ),
            "-F",
            "run.py",
        ],
        cwd="commandfrog",
        check=True,
    )

    subprocess.run("cp commandfrog/dist/run commandfrog-builds/commandfrog", check=True, shell=True)
