from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = ()
keyboard.row_pins = (10, 9, 8)

keyboard.keymap = [
    [
        KC.LGUI(KC.C),  # Copy
        KC.LGUI(KC.V),  # Paste
        KC.LGUI(KC.Z),  # Undo
    ]
]

if __name__ == '__main__':
    keyboard.go()