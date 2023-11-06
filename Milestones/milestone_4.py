import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = str(random.choice(word_list))
        self.word_guessed = ['_' for letter in list(self.word)]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = set()

        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")
    

    def check_guess(self, letter) -> None:
        self.list_letters.add(letter.lower())
        index = -1
        letter_found = False
        for ch in list(self.word.lower()):
            index = index + 1
            if ch == letter.lower():
                letter_found = True
                self.word_guessed[index] = letter.lower()
        if letter_found == True:
            self.num_letters = self.num_letters - 1
            print("Well done, you guessed a letter!")
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1
            print(f"You have {self.num_lives} lives left!")
        

    def check_letter(self):
            while self.num_lives != 0:
                print(self.num_letters)
                guess = input("Please enter your letter:")
                if len(guess) != 1 or not guess.isalpha():
                    print("Please, enter just one character")
                elif guess.lower() in self.list_letters:
                    print(f"Letter {guess} was already tried, please try again!")
                else:
                    self.check_guess(guess)
                if self.num_letters == 0:
                    print(f"Well done, you won the game with {self.num_lives} left!")
                    break
            else:
                print("You have lost all your lives!")

    
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.check_letter()


if __name__ == '__main__':
    word_list = ['Banana', 'Apple', 'Orange', 'Peach', 'Pear']
    play_game(word_list)
