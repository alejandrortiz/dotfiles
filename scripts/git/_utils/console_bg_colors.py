class ConsoleBgColors(object):
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def warning(text) -> str:
        return ConsoleBgColors.ORANGE + text + ConsoleBgColors.ENDC

    @staticmethod
    def success(text) -> str:
        return ConsoleBgColors.GREEN + text + ConsoleBgColors.ENDC

    @staticmethod
    def info(text) -> str:
        return ConsoleBgColors.BLUE + text + ConsoleBgColors.ENDC

    @staticmethod
    def error(text) -> str:
        return ConsoleBgColors.FAIL + text + ConsoleBgColors.ENDC


if __name__ == "__main__":
    sys.exit(1)
