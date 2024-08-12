import random

class Hangman:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        guess = input("Enter a letter to guess: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter.")
            return

        self.turn_count += 1
        if guess in self.word_to_find:
            for index, letter in enumerate(self.word_to_find):
                if letter == guess:
                    self.correctly_guessed_letters[index] = guess
        else:
            if guess not in self.wrongly_guessed_letters:
                self.wrongly_guessed_letters.append(guess)
                self.error_count += 1
                self.lives -= 1

        print(f"Correctly guessed letters: {' '.join(self.correctly_guessed_letters)}")
        print(f"Wrongly guessed letters: {', '.join(self.wrongly_guessed_letters)}")
        print(f"Lives left: {self.lives}")
        print(f"Error count: {self.error_count}")
        print(f"Turn count: {self.turn_count}")

    def start_game(self):
        while self.lives > 0:
            self.play()
            if '_' not in self.correctly_guessed_letters:
                return self.well_played()
        return self.game_over()

    def game_over(self):
        print("Game over...")
        print(f"The word was: {''.join(self.word_to_find)}")

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")

if __name__ == "__main__":
    game = Hangman()
    game.start_game()
