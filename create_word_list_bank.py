# Create a word list and word bank to use in a game of Wordle.

import json
from nltk.corpus import brown, words
from nltk.probability import FreqDist

# Create word bank using 1000 most common words in Brown corpus
word_bank = [
    word
    for word in brown.words()
    if len(word) == 5
    and word.isalpha()  # to weed out numbers, contractions, etc.
    and word.islower()  # to weed out proper names
]
word_bank = [freq[0] for freq in FreqDist(word_bank).most_common()[:1000]]
word_bank = [word.upper() for word in word_bank]

# Create word list using words corpus
word_list = [
    word
    for word in words.words()
    if len(word) == 5
    and word.isalpha()  # to weed out numbers, contractions, etc.
    and word.islower()  # to weed out proper names
]
word_list += word_bank  # to ensure that word list contains word bank
word_list = list(set(word_list))  # to remove duplicates
word_list = [word.upper() for word in word_list]
assert set(word_bank).issubset(set(word_list))

with open("word_list.json", "w") as file:
    json.dump(word_list, file)
with open("word_bank.json", "w") as file:
    json.dump(word_bank, file)
