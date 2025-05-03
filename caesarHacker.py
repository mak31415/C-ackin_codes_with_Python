# Caesar encryption cracking program
# BSD Licensed

import pyperclip

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)
            translated += SYMBOLS[translatedIndex]
        else:
            translated += symbol
    # Copy the translated message to the clipboard

    print(f'Key {key}: {translated}')
