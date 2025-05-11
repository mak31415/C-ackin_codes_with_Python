# Transposition Cipher Decryption Program
# BSD Licensed

import pyperclip, math

def main():
  myMessage = 'Cenoonommstmme oo snnio. s s c'
  mykey = 8

  plaintext = decryptMessage(mykey, myMessage)

  print(plaintext + '|')
  pyperclip.copy(plaintext)
  print('The decrypted message is copied to the clipboard.')

def decryptMessage(key, message):
  numColumns = int(math.ceil(len(message) / float(key)))
  numOfRows = key
  numOfShadedBoxes = (numColumns * numOfRows) - len(message)
  
  plaintext = [''] * numColumns
  column = 0
  row = 0

  for symbol in message:
    plaintext[column] += symbol
    column += 1

    if (column == numColumns) or (column == numColumns - 1 and row >= numOfRows - numOfShadedBoxes):
      column = 0
      row += 1

  return ''.join(plaintext)
    

if __name__ == '__main__':
  main()