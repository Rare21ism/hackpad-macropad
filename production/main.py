{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww29200\viewh14900\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from kmk.kmk_keyboard import KMKKeyboard\
from kmk.keys import KC\
\
keyboard = KMKKeyboard()\
\
keyboard.col_pins = ()\
keyboard.row_pins = (10, 9, 8)\
\
keyboard.keymap = [\
    [\
        KC.LGUI(KC.C),  # Copy\
        KC.LGUI(KC.V),  # Paste\
        KC.LGUI(KC.Z),  # Undo\
    ]\
]\
\
if __name__ == '__main__':\
    keyboard.go()}