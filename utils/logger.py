from colorama import Fore, Style

class Logger:
    def log(self, message):
        print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} {message}")
