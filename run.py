# proj:   handfree
# file:   run.py
# author: Mark Sabini (GitHub: ShinyCode)
# desc:   Run this file to experience the joy of one-handed typing.
# ------------------------------------
from __future__ import print_function
import keyboard
import layout

def main():
    layout.layout_basic()
    print('HandFree is running. To exit, close this window or press [ctrl] + [c].')
    print('Enjoy the blissful liberation of one-handed typing!')
    keyboard.wait()

if __name__ == '__main__':
    main()
