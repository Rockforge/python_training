# exercise44.py
import argparse

parser = argparse.ArgumentParser(description='Spams the word spam')
parser.add_argument('repeats', type=int, help='number of times to repeat the word')
parser.add_argument('--word', default='spam', dest='word_to_use')

args = parser.parse_args()
repeats = args.repeats
word = args.word_to_use

print(word * repeats)