RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RED_BG = "\033[101m"
GREEN_BG = "\033[42m"
BLUE_BG = "\033[104m"
YELLOW_BG = "\033[103m"
RESET = "\033[0m"


class logger:
    @staticmethod
    def fail(msg: str, highlight: bool = False):
        if highlight:
            print(f"{RED_BG}[FAIL]{RESET} {BOLD}{RED}{msg}{RESET}")
        else:
            print(f"{RED_BG}[FAIL]{RESET} {msg}{RESET}")

    @staticmethod
    def warn(msg: str, highlight: bool = False):
        if highlight:
            print(f"{YELLOW_BG}[WARN]{RESET} {BOLD}{YELLOW}{msg}{RESET}")
        else:
            print(f"{YELLOW_BG}[WARN]{RESET} {msg}{RESET}")

    @staticmethod
    def info(msg: str, highlight: bool = False):
        if highlight:
            print(f"{BLUE_BG}[INFO]{RESET} {BOLD}{BLUE}{msg}{RESET}")
        else:
            print(f"{BLUE_BG}[INFO]{RESET} {msg}{RESET}")

    @staticmethod
    def success(msg: str, highlight: bool = False):
        if highlight:
            print(f"{GREEN_BG}[PASS]{RESET} {BOLD}{GREEN}{msg}{RESET}")
        else:
            print(f"{GREEN_BG}[PASS]{RESET} {msg}{RESET}")
