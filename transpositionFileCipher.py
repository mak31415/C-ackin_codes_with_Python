# Encrypting/Decrypting Files Using Transposition Cipher
# Bsd Licensed

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
  inputFilename = 'frankenstein.encrypted.txt'
  outputFilename = 'frankenstein.decrypted.txt'
  mykey = 10
  myMode = 'decrypt' # Set to 'decrypt' to decrypt the file

  if not os.path.exists(inputFilename):
    print('The file %s does not exist. Please check the filename and try again.' % (inputFilename))
    sys.exit()

  if os.path.exists(outputFilename):
    print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %(outputFilename))
    response = input('> ')
    if not response.lower().startswith('c'):
      print('Quitting...')
      sys.exit()

  
  fileObj = open(inputFilename)
  content = fileObj.read()
  fileObj.close()

  print('%sing...' % (myMode.title()))

  setartTime = time.time()
  if myMode == 'encrypt':
    translated = transpositionEncrypt.encryptMessage(mykey, content)
  elif myMode == 'decrypt':
    translated = transpositionDecrypt.decryptMessage(mykey, content)

  totalTime = round(time.time() - setartTime, 2)
  print('The %sion took %s seconds.' % (myMode, totalTime))

  outputFileObj = open(outputFilename, 'w')
  outputFileObj.write(translated)
  outputFileObj.close()

  print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
  print('%sed file is %s.' % (myMode.title(), outputFilename))

if __name__ == '__main__':
  main()
  print('Done.')
  input('Press Enter to exit.')

