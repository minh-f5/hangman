# Hangman Game

A Python implementation of the classic Hangman game.

## Overview

The Hangman game is a word-guessing game where the player tries to guess a word one letter at a time. The player has a limited number of incorrect guesses allowed before the game is lost.

## Class `hangman`

This class represents the Hangman game.

### Attributes

- `word` (list): A list of words. One of these words will be selected as the word to guess.
- `lives` (int): The number of lives the player has left. It starts at 5.
- `turn_count` (int): The number of turns played by the player.
- `error_count` (int): The number of errors made during the game.
- `correctly_guessed_letters` (list of str): A list of letters that the user has guessed correctly.
- `wrongly_guessed_letters` (list of str): A list of letters that the user has guessed incorrectly.
- `word_to_find` (list of str): The word to be guessed, represented as a list of its letters.

### Methods

#### `__init__(self, lives)`

Initializes the Hangman game with a random word, sets the lives, and initializes other attributes.

- **Parameters:**
  - `lives` (int): The number of lives the player has.

#### `play(self, guess: str) -> str`

Processes the player's guess.

- **Parameters:**
  - `guess` (str): The letter guessed by the player.

- **Returns:**
  - The guessed letter.

#### `start_game(self) -> str`

Starts the Hangman game. It keeps running until the player runs out of lives or guesses the word correctly.

- **Returns:**
  - A string indicating the game result (either "Game over!" or a message indicating the word was found).

#### `game_over(self) -> str`

Ends the game and returns "Game over!".

- **Returns:**
  - "Game over!"

#### `well_played(self) -> str`

Returns a message indicating the word was found, the number of turns taken, and the number of errors made.

- **Returns:**
  - A string indicating the word was found, the number of turns taken, and the number of errors made.

## Example Usage

```python
game = hangman(lives=5)
game.start_game()
```
