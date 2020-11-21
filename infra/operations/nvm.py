from infra.drivers.driver import Driver
from .script import script_from_string
from .shell import get_shell_rc_file

nvm_init_script = [
    '''export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"''',
    '''[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"'''
]

def install_nvm(host: Driver) -> None:
    """
    Download and install nvm. Add the commands for auto-loading it to the rc
    file for the particular shell (if it's a shell we recognise).
    """
    stdout = host.exec("test -f ~/.nvm/nvm.sh > /dev/null; echo $?").stdout
    if stdout.decode().strip() == "0":
        return

    host.exec("apt-get install -y curl", sudo=host.has_sudo)
    host.exec("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.36.0/install.sh | bash")

    host.exec(script_from_string(host, src="\n".join(nvm_init_script)))

    rc_file = get_shell_rc_file(host)
    if rc_file is not None:
        if host.exec(f"grep NVM_DIR {rc_file}").return_code != 0:
            for i, line in enumerate(nvm_init_script):
                host.exec(script_from_string(host, "\n".join([
                    f"cat >> {rc_file} <<EOF",
                    *nvm_init_script,
                    "EOF",
                ])))


def nvm_install(host: Driver, node_version: str):
    """
    Use nvm to install version `node_version` of node. Eg.
    `nvm_install("v13.7.0")`. Any version that appears in the list output when
    you run `nvm ls` should work.
    """
    install_nvm(host)
    host.exec(script_from_string(host, src="\n".join([*nvm_init_script, f"nvm install {node_version}"])))


def npm_install(host: Driver, node_version: str, cwd: str):
    """
    Run `npm install` in the directory `cwd`, after executing `nvm use
    {node_version}`.
    """
    host.exec(script_from_string(host, src="\n".join([
        *nvm_init_script,
        f"nvm use {node_version}",
        f"cd {cwd}",
        "npm install"
    ])))




