# proj:   handfree
# file:   util.py
# author: Mark Sabini (GitHub: ShinyCode)
# desc:   A bunch of callbacks used for remapping keys.
# ------------------------------------
from __future__ import print_function
import keyboard

def cb_key(keyL, keyU, keyCL, keyCU, dir=None):
    sckeyL = min(keyboard.key_to_scan_codes(keyL))
    sckeyU = min(keyboard.key_to_scan_codes(keyU))
    sckeyCL = min(keyboard.key_to_scan_codes(keyCL))
    sckeyCU = min(keyboard.key_to_scan_codes(keyCU))
    def cb_key_fn(e):
        if keyboard.is_pressed('capslock'):
            if keyboard.is_pressed('shift'):
                keyboard.press_and_release(sckeyCU)
            elif keyboard.is_pressed('tab') and dir is not None:
                keyboard.press_and_release(dir)
            else:
                keyboard.press_and_release(sckeyCL)
        else:
            if keyboard.is_pressed('shift'):
                keyboard.press_and_release(sckeyU)
            else:
                keyboard.press_and_release(sckeyL)
    return cb_key_fn

def cb_key_raw(keyL, keyU, keyCL, keyCU, dir=None):
    def cb_key_fn(e):
        if keyboard.is_pressed('capslock'):
            if keyboard.is_pressed('shift'):
                keyboard.press_and_release(keyCU)
            elif keyboard.is_pressed('tab') and dir is not None:
                keyboard.press_and_release(dir)
            else:
                keyboard.press_and_release(keyCL)
        else:
            if keyboard.is_pressed('shift'):
                keyboard.press_and_release(keyU)
            else:
                keyboard.press_and_release(keyL)
    return cb_key_fn

# Do nothing! Useful for just suppressing a key.
def cb_nop(e):
    pass

# Slightly hacky callback for tab, to enable [capslock] + [tab] combos
def cb_tab(e):
    if not keyboard.is_pressed('capslock'):
        keyboard.press_and_release('tab')
