#! /usr/bin/env python3
# bullet_point_adder.py - prefixes bullet points to each line of text on the clipboard

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

# prefixes each individual line with '* '
lines = ['* ' + line for line in lines]

# joins the split lines back together and pastes to clipboard
text = '\n'.join(lines)
pyperclip.copy(text)
