import sys
from abc import abstractmethod, ABCMeta


class GitError(Exception):
    __metaclass__ = ABCMeta

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

    @abstractmethod
    def error_message(self) -> str:
        pass


class VersionNotFound(GitError):
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        # Call the base class constructor with the parameters it needs
        super().__init__(self.error_message())

    def error_message(self) -> str:
        return 'Version not found in <%s> path' % self.base_dir


class VersionAlreadyExist(GitError):
    def __init__(self, version: str):
        self.version = version
        # Call the base class constructor with the parameters it needs
        super().__init__(self.error_message())

    def error_message(self) -> str:
        return 'Version <%s> tag already exist' % self.version


if __name__ == "__main__":
    sys.exit(1)
