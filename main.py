#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script for automate typing tests,
# in test sites.
# cheating in sites like typing racer.
# note the website that i use for this script:
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
from pynput.keyboard import Key, Controller
from time import sleep


def clear():
    """wipe the terminal screen"""

    if os_name == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def typing(msg: str, period: int = 250e-3):
    """this function will type the msg using,
    the physical keyboard."""

    # create the main Keyboard controller object.
    keyboard = Controller()

    for char in msg:
        keyboard.press(char)
        sleep(period)


def main():

    sleep(15)

    msg = "To learn to type quickly, practice often and adopt the proper technique. Fix your posture, have adequate lighting, position your hands correctly over the keyboard, look at the screen and use all your fingers to hit the keys. At first, concentrate on accuracy over speed. This will help you develop muscle memory and create automatic reflexes. Keep practicing and gradually pick up the pace. You'll see results after just a few weeks! To learn to type quickly, practice often and adopt the proper technique. Fix your posture, have adequate lighting, position your hands correctly over the keyboard, look at the screen and use all your fingers to hit the keys. At first, concentrate on accuracy over speed. This will help you develop muscle memory and create automatic reflexes. Keep practicing and gradually pick up the pace. You'll see results after just a few weeks!"
    typing(msg, period=50e-3)


if __name__ == "__main__":
    main()
