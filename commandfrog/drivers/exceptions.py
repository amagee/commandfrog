class CommandFailed(Exception):
    def __init__(self, cmd):
        self.cmd = cmd
