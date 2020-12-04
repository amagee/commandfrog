import subprocess
from pathlib import Path
from functools import reduce
import operator


def build():
    subprocess.run("rm -rf dist", cwd="commandfrog", check=True, shell=True)

    operations = [p.stem for p in (Path("commandfrog") / "operations").glob("*.py")]

    subprocess.run(
        [
            "pyinstaller",
            *reduce(
                operator.iconcat, 
                [["--hidden-import", f"commandfrog.operations.{f}"] for f in operations]
            ),
            "-F",
            "commandfrog.py",
        ],
        cwd="commandfrog",
        check=True,
    )
    
    subprocess.run("cp dist commandfrog-builds", cwd="commandfrog", check=True, shell=True)
