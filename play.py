# Play a game of Wordle.

import json
from wordle_game import WordleGame

with open("word_list.json", "r") as file:
    word_list = json.load(file)
with open("word_bank.json", "r") as file:
    word_bank = json.load(file)

game = WordleGame(word_list, word_bank)
game.play_game()
