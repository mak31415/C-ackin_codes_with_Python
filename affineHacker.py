# Program for cracking affine cipher
# License BSD

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False  # Set to True to disable output to console


def main():
  myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQ
QQQQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Q
QQQQda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

  hackedMessage = hackAffine(myMessage)

  if hackedMessage != None:
    print('Copying hacked message to clipboard:')
    print(hackedMessage)
    pyperclip.copy(hackedMessage)
  else:
    print('Failed to hack the message.')


def hackAffine(message):
  
  print('Hacking...')
  print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

  for key in range(len(affineCipher.SYMBOLS) ** 2):
    keyA = affineCipher.getKeyParts(key)[0]
    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
      continue

    decryptedText = affineCipher.decryptMessage(key, message)

    if not SILENT_MODE:
      print('Tried Кеу %s". (%s)' % (key, decryptedText[:40]))

    if detectEnglish.isEnglish(decryptedText):
      print()
      print('Possible encryption hack:')
      print('Key: %s' % (key))
      print('Decrypted message: ' + decryptedText[:200])
      print()
      print ( ' Enter D if done, anything else to continue hacking : ' )
      response = input('> ')

      if response.strip().upper().startswith('D'):
        return decryptedText
  print('Failed to hack the message.')
  return None


if __name__ == '__main__':
  main()
  