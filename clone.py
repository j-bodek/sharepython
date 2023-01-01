import subprocess
import os
import sys


def main():
    """
    This function is used to cloning microservices
    repositories automatically
    """

    class colors:
        YELLOW = "\033[33m"
        GREEN = "\033[32m"
        ENDC = "\033[m"

    services = [
        ("https://github.com/LilJack118/sharepython-frontend.git", "frontend"),
        ("https://github.com/LilJack118/sharepython-api.git", "api"),
        (
            "https://github.com/LilJack118/sharepython-websocket-server.git",
            "websocket_server",
        ),
    ]

    def git(*args):
        return subprocess.check_call(["git"] + list(args))

    for repo, name in services:
        if not os.path.isdir(name):
            sys.stdout.write(
                colors.GREEN + f"Cloning {name} repository\n" + colors.ENDC
            )
            # clone repository and rename it
            git("clone", repo, name)
        else:
            sys.stdout.write(colors.YELLOW + f"{name} folder exist\n" + colors.ENDC)


if __name__ == "__main__":
    main()
