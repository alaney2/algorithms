import hashlib
# from english_words import english_words_set
import nltk
nltk.download()
from nltk.corpus import words
word_list = words.words()
print(len(word_list))

HASH = '7e3261e24381ac38020ba88a06c686d1'
SALT = '49b19aaeb7fc'
def decode():
  for word in word_list:
    if len(word) != 7:
      continue
    pre = SALT + word
    guess = hashlib.md5(pre.encode('utf-8')).hexdigest()
    if guess.lower() == HASH or guess == HASH:
      print('Password found:', word)
      # return
    post = word + SALT
    guess = hashlib.md5(post.encode('utf-8')).hexdigest()
    if guess.lower() == HASH or guess == HASH:
      print('Password found:', word)
      # return
  print('Password not found')

decode()