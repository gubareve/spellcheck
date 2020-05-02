"""
similar

Description: Gives similar words
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def findsimilar(word):  #Generates Similar Words that may or may not be real words.
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return deletes + transposes + replaces + inserts
