# Play a game of Wordle.

from wordle_game import WordleGame

# Load word list and word bank
# source: https://github.com/Kinkelin/WordleCompetition/tree/main/data/official
with open("combined_wordlist.txt", "r") as f:
    word_list = [line.upper() for line in f.read().splitlines()[1:]]
with open("shuffled_real_wordles.txt", "r") as f:
    word_bank = [line.upper() for line in f.read().splitlines()[1:]]

game = WordleGame(word_list, word_bank)
game.play_game()
