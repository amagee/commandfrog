# commandfrog

Inspired by [pyinfra](https://pyinfra.com/), itself inspired by tools such as
[Ansible](https://www.ansible.com/), commandfrog is a very simple automation
tool. It's optimised for simplicity and predictability over performance.
commandfrog is great for tasks like setting up development environments, or
running deployments on reasonably small number of machines. If you have huge
numbers of machines, a more high-performance tool like pyinfra might be more
appropriate.

## Getting started

    # Scripts are just Python files
    cat >install_neovim.py <<EOF
    from commandfrog.operations.apt import apt_install

    def install_neovim(host):
        apt_install(host, ["neovim"])
        host.exec("nvim") # Run neovim now because why not
    EOF

    # We have some pyinfra-like sudo management, which is turned off by default.
    # Turn it on:
    cat >config.yml <<EOF
    ask_for_sudo_password: true
    EOF

    # From source:
    # Install:
    git clone https://github.com/amagee/commandfrog.git
    cd commandfrog
    pip install poetry
    poetry install

    # Run our script to install neovim locally
    python commandfrog/commandfrog.py @local install_neovim.py:install_neovim --config=config.yml

    # Or, use the pre-built binary (Currently built for Linux only)
    wget https://raw.githubusercontent.com/amagee/commandfrog-builds/main/commandfrog
    chmod +x commandfrog
    ./commandfrog @local install_neovim.py:install_neovim --config=config.yml

commandfrog can run on:

* Your local machine (with `@local`) as above
* Over SSH (with a value like `youruser@hostname`; `yourusername@localhost`
  should behave similarly to `@local`)
* On docker containers. You can specify an image (eg. `@docker/ubuntu` to start 
  a new container based on the image, or `@docker/some_container_id` to run in
  an already-running container).

The commands to run must come from a Python file, which can be anywhere on your
file system (not necessarily on your `PYTHONPATH`, and note that the *file
path* is specified, not a Python module path. The argument should be of the
form `path:function_name` where `function_name` is a top-level function in the
Python file.

Currently config, if specified at all, must be in a YAML file. The only
configuration parameter recognised by commandfrog is `ask_for_sudo_password`,
which is false by default (useful for Docker images where you're running as
root or on machines where the user has passwordless sudo). However, you can add
arbitrary parameters to the config file and access them in your function. For example,

    cat >config.yml <<EOF
    myparam1: 123
    myparam2: {
      "key": "val"
    }
    EOF

    cat >print_params.py <<EOF
    def print_params(host):
        print(host.config.myparam1)
        print(host.config.myparam2)
    EOF

    python commandfrog/commandfrog.py @local print_params.py:print_params --config=config.yml

will print

    123
    {'key': 'val'}

Note that the top-level parameters in the config file turn into *properties* in
the `host.config` object, not keys. But this is not done recursively, so if you have
a property whose value is a dictionary, then it will be a dictionary in the config object.
 

