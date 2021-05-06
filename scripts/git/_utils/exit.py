import sys


class Exit(object):
    @staticmethod
    def wrong():
        sys.exit(1)

    @staticmethod
    def fine():
        sys.exit(0)
