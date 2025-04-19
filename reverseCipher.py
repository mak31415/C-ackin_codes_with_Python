# Reverse encryption program
# BSD Licensed


message = input("Enter a message to be reversed: ")
translated = ""

i = len(message) - 1;
while i >= 0:
  translated = translated + message[i]
  i = i - 1

print(translated)

