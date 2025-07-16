# Caesar encryption cracking program
# BSD Licensed

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

(0...SYMBOLS.length).each do |key|
  translated = ''

  message.each_char do |symbol|
    if SYMBOLS.include?(symbol)
      symbol_index = SYMBOLS.index(symbol)
      translated_index = symbol_index - key
      if translated_index < 0
      translated_index += SYMBOLS.length
      end
    translated += SYMBOLS[translated_index]
    else
      translated += symbol  # Add the symbol without change
    end
  end

  puts "Key #{key}: #{translated}"
end
