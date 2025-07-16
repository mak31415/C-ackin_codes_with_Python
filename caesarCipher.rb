# Caesar cipher
# This program encrypts and decrypts a message using the Caesar cipher.
# BSD Licensed

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# Key for the Caesar cipher
key = 13

mode = 'decrypt' # Change to 'decrypt' to decrypt the message

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

message.each_char do |symbols|
  
  if SYMBOLS.include?(symbols)

    symbolIndex = SYMBOLS.index(symbols)

    if mode == 'encrypt'
      translatedIndex = symbolIndex + key
    elsif mode == 'decrypt'
      translatedIndex = symbolIndex - key
    end
    if translatedIndex >= SYMBOLS.length
      translatedIndex -= SYMBOLS.length
    elsif translatedIndex < 0
      translatedIndex += SYMBOLS.length
    end
    translated += SYMBOLS[translatedIndex]
  else
    translated += symbols  # Add the symbol without change
  end
end

puts "#{mode.capitalize}ed message: #{translated}"
# Output the translated message