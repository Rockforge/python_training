# exercise5.py

# strings are always case sensitive
sentence = 'the quick brown FOX jumps over the lazy dog'

print(sentence.upper())
print(sentence.lower())
print(sentence.swapcase())
print(sentence.title())
print(sentence.count('u'))
print(sentence.replace('fox', 'cat'))
print(sentence.replace('FOX', 'elephant'))
print(sentence.replace(" ", "_"))
print(len(sentence))