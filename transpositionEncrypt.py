# Transposition Cipher Encryption Program
# BSD Licensed

import pyperclip

def main():
  myMessage = 'Common sense is not so common.'
  mykey = 8

  chifertext = encryptMessage(mykey, myMessage)
  print('Ciphertext:')
  print(chifertext + '|')
  pyperclip.copy(chifertext)
  print('Ciphertext copied to clipboard.')

def encryptMessage(key, message):
  ciphertext = [''] * key

  for column in range(key):
    currentIndex = column

    while currentIndex < len(message):
      ciphertext[column] += message[currentIndex]

      currentIndex += key

  return ''.join(ciphertext)

if __name__ == '__main__':
  main()
