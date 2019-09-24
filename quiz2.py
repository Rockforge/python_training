# quiz2.py

# Make a program that removes all vowels using replace function and for loops
# Print the sentence

sentence = 'the quick brown fox jumps over the lazy dog'

for vowel in ['a', 'e', 'i', 'o', 'u']: 
    sentence = sentence.replace(vowel, '')

print(sentence)

