import sys

from _utils.console_bg_colors import ConsoleBgColors


class Console(object):
    def __init__(self, verbose: bool):
        self.verbose = verbose

    def log(self, message: str) -> None:
        if self.verbose:
            print("[] %s" % message)

    def info(self, message: str) -> None:
        if self.verbose:
            print(ConsoleBgColors.info("[] %s" % message))

    def success(self, message: str) -> None:
        if self.verbose:
            print(ConsoleBgColors.success("[] %s" % message))

    def error(self, message: str) -> None:
        if self.verbose:
            print(ConsoleBgColors.error("[] %s" % message))


if __name__ == "__main__":
    sys.exit(1)
