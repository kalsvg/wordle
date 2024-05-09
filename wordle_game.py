# Define a class representing a game of Wordle.

import os
import time
import random
from colorama import Fore, Back, Style


class WordleGame:

    def __init__(self, word_list, word_bank, word=None):
        self.word_list = word_list
        self.word_bank = word_bank
        self.word_length = 5
        self.word = word
        self.n_guesses = 6
        self.turn = 0
        self.guesses = ["*" * self.word_length for i in range(self.n_guesses)]
        self.colors = [
            [Back.WHITE + Fore.BLACK] * self.word_length for i in range(self.n_guesses)
        ]
        self.game_over = False
        self.game_won = False

    def __clear_screen(self) -> None:
        """Clear the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def __pick_word(self) -> None:
        """Pick a random word from the word bank."""
        self.word = random.choice(self.word_bank)

    def __get_guess(self) -> str:
        """Prompt the user for a guess."""
        while True:
            guess = input("Make a guess: ").upper()
            if len(guess) != self.word_length:
                print(
                    f"Oops, a guess needs to have {self.word_length} letters. "
                    + "Please try again!"
                )
            elif guess not in self.word_list:
                print("Oops, that isn't in the word list. Please try again!")
            elif guess in self.guesses:
                print("Oops, that word has already been guessed. Please try again!")
            else:
                return guess

    def __get_colors(self, guess: str) -> list:
        """Get colors for the guess."""
        colors = [Back.LIGHTBLACK_EX + Fore.WHITE] * self.word_length
        letters_list = [letter for letter in self.word]
        # Determine green letters
        for position, letter in enumerate(guess):
            if self.word[position] == letter:
                colors[position] = Back.GREEN + Fore.WHITE
                letters_list.remove(letter)
        # Determine yellow letters
        for position, letter in enumerate(guess):
            if self.word[position] != letter:
                if letter in letters_list:
                    colors[position] = Back.YELLOW + Fore.WHITE
                    letters_list.remove(letter)
        return colors

    def display_guesses(self) -> None:
        """Display the guesses."""
        for guess, color in zip(self.guesses, self.colors):
            for i in range(self.word_length):
                print(color[i] + f" {guess[i]} ", end="")
            print()
        print(Style.RESET_ALL)

    def play_game(self) -> None:
        """Play the game."""
        if self.game_over == True:
            raise ValueError("game is over.")
        if self.word == None:
            self.__pick_word()
        while not self.game_over:
            self.__clear_screen()
            self.display_guesses()
            guess = self.__get_guess()
            self.guesses[self.turn] = guess
            self.colors[self.turn] = self.__get_colors(guess)
            if guess == self.word:
                self.game_won = True
                self.game_over = True
            elif self.turn == self.n_guesses - 1:
                self.game_over = True
            else:
                self.turn += 1
        self.__clear_screen()
        self.display_guesses()
        if self.game_won:
            print("You win!")
        else:
            print(f"Sorry, you lose. The word was {self.word}.")
        print("Thanks for playing.\n")
