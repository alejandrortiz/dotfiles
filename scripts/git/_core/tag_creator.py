import json
import os
import sys
from typing import Optional
from git import Repo

from _utils.console import Console
from _utils.exit import Exit

from _core.exception import GitError, VersionNotFound, VersionAlreadyExist


class TagCreator(object):
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.console = Console(verbose)

    def create(self, base_dir: str, input_version: Optional[str]) -> dict:
        repo: Repo = Repo(base_dir)
        commit = repo.commit(repo.head)
        version: str = self.project_version(base_dir)

        if version is None and input_version is not None:
            version = input_version

        if version is None:
            raise VersionNotFound(base_dir)

        version_formatted: str = self.format_version(version)

        if (len(repo.tags)) == 0:
            latest_version = ''
        else:
            latest_version = repo.tags[len(repo.tags) - 1]

        if latest_version != '' and version_formatted == str(latest_version):
            raise VersionAlreadyExist(latest_version)

        repo.create_tag(version_formatted, commit, 'Version %s' % version_formatted)
        repo.remote().push(version_formatted)

        return dict(
            version=version_formatted,
            commit_checksum=commit.hexsha,
            commit_author=commit.author,
            commit_message=commit.message
        )

    def format_version(self, version: str) -> str:
        if not version.startswith('v'):
            return "v{}".format(version)

        return version

    def project_version(self, base_dir: str) -> Optional[str]:
        if os.path.isfile(base_dir + '/composer.json'):
            return self.php_project_version(base_dir)
        else:
            return None

    def php_project_version(self, base_dir: str) -> Optional[str]:
        with open(base_dir + '/composer.json', 'r') as composer_file:
            composer_data: dict = json.load(composer_file)

            if 'version' in composer_data:
                return composer_data['version']
            else:
                return None


if __name__ == "__main__":
    sys.exit(1)
