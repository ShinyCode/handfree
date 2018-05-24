# proj:   handfree
# file:   layout.py
# author: Mark Sabini (GitHub: ShinyCode)
# desc:   This file defines remappings/layouts/special behavior.
# ------------------------------------
from __future__ import print_function
import keyboard
import util

# function: caps_remap
# Basic function for remapping a key. If this doesn't work, try caps_remap_raw!
# Params: key:   [target key]
#         keyL:  [keypress]
#         keyU:  [shift] + [keypress]
#         keyCL: [capslock] + [keypress]
#         keyCU: [capslock] + [shift] + [keypress]
#         dir:   [capslock] + [tab] + [keypress]
def caps_remap(key, keyL, keyU, keyCL, keyCU, dir=None):
    keyboard.on_press_key(key, util.cb_key(keyL, keyU, keyCL, keyCU, dir), suppress=True)

# function: caps_remap_raw
# Basic function for remapping a key. If this doesn't work, try caps_remap!
# Params: Same as caps_remap.
def caps_remap_raw(key, keyL, keyU, keyCL, keyCU, dir=None):
    keyboard.on_press_key(key, util.cb_key_raw(keyL, keyU, keyCL, keyCU, dir), suppress=True)

# function: layout_basic
# A basic layout based loosely off of https://blog.xkcd.com/2007/08/14/mirrorboard-a-one-handed-keyboard-layout-for-the-lazy/.
def layout_basic():
    # Remap keys
    caps_remap('`', 'backspace', 'backspace', '`', '~')
    caps_remap_raw(2, '1', '!', '7', '&') # Remap keys 1-6
    caps_remap_raw(3, '2', '@', '8', '*')
    caps_remap_raw(4, '3', '#', '9', '(')
    caps_remap_raw(5, '4', '$', '0', ')')
    caps_remap_raw(6, '5', '%', '-', '_')
    caps_remap_raw(7, '6', '^', '=', '+')

    caps_remap('q', 'q', 'Q', 'p', 'P', 'volume mute')
    caps_remap('w', 'w', 'W', 'o', 'O', 'up')
    caps_remap('e', 'e', 'E', 'i', 'I', 'volume down')
    caps_remap('r', 'r', 'R', 'u', 'U', 'volume up')
    caps_remap('t', 't', 'T', '[', '{')
    caps_remap('y', 'y', 'Y', ']', '}')
    caps_remap('u', 'u', 'U', '\\', '|')

    caps_remap('a', 'a', 'A', ';', ':', 'left')
    caps_remap('s', 's', 'S', 'l', 'L', 'down')
    caps_remap('d', 'd', 'D', 'k', 'K', 'right')
    caps_remap('f', 'f', 'F', 'j', 'J')
    caps_remap('g', 'g', 'G', '\'', '"')
    caps_remap('h', 'h', 'H', 'enter', 'enter')

    caps_remap('z', 'z', 'Z', '.', '<')
    caps_remap('x', 'x', 'X', ',', '>')
    caps_remap('c', 'c', 'C', 'm', 'M')
    caps_remap('v', 'v', 'V', 'n', 'N')
    caps_remap('b', 'b', 'B', '?', '/')

    # Bind key-specific callbacks
    keyboard.on_press_key('capslock', util.cb_nop, suppress=True)
    keyboard.on_press_key('tab', util.cb_tab, suppress=True)
