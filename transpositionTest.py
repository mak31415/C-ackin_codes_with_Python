# Testing a Transposition Cipher

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42)  # Set a seed for reproducibility

    for i in range(20):
        message = 'AВCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        for key in range(1, int(len(message) / 2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print('Misrnatch with key %s and rnessage %s.' % (key, message))
                print('Decrypted as:' + decrypted)
                sys.exit()

    print(' Transposition cipher test passed . ')


if __name__ == '__main__':
    main() 