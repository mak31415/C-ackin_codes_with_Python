# Caesar cipher
# This program encrypts and decrypts a message using the Caesar cipher.
# BSD Licensed

import pyperclip

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# Key for the Caesar cipher
key = 13

mode = 'decrypt'  # Set to 'decrypt' to decrypt the message

# Symbols used in the cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in message:
    # Encrypt or decrypt the symbol
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        # Wrap around if the index is out of bounds
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)
        translated += SYMBOLS[translatedIndex]
    else:
        # If the symbol is not in SYMBOLS, just add it to translated
        translated += symbol
# Copy the translated message to the clipboard
print(translated)
pyperclip.copy(translated)  
