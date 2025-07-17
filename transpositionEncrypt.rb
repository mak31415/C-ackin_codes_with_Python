# Transposition Cipher Encryption Program
# BSD Licensed

require_relative 'pyperclip'

def main()
  myMessage = 'Common sense is not so common.'
  mykey = 8

  ciphertext = transpositionEncrypt(myMessage, mykey)

  puts "Ciphertext: #{ciphertext} |"
  RubyClip.copy(ciphertext)
  puts "Ciphertext copied to clipboard."
end

def transpositionEncrypt(message, key)
  ciphertext = [''] * key

  message.chars.each_with_index do |char, index|
    column = index % key
    ciphertext[column] += char
  end

  ciphertext.join
end

if __FILE__ == $0
  main()
end
