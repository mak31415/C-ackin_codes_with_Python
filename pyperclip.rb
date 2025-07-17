module RubyClip
  ENCODING = 'UTF-8'

  def self.copy(text)
    IO.popen('pbcopy', 'w') { |f| f.write(text.to_s.encode(ENCODING)) }
  end

  def self.paste
    `pbpaste`.force_encoding(ENCODING)
  end

  def self.available?
    system('which pbcopy > /dev/null') && system('which pbpaste > /dev/null')
  end
end
