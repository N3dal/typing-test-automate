#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script for automate typing tests,
# in test sites.
# cheating in sites like typing racer.
# note the website that i use for this is:
# "https://www.typingpal.com/en/typing-test"
#
#
# Author:N84.
#
# Create Date:Sun Mar  6 16:36:53 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import system
from os import name as os_name


def clear():
    """wipe the terminal screen"""

    if os_name == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def main():
    pass


if __name__ == "__main__":
    main()
