import random

class Hangman:

    #Initialises the variables required for the game 
    def __init__(self, word_list, num_lives=5):
        self.word = str(random.choice(word_list))
        self.word_guessed = ['_' for letter in list(self.word)]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = set()

        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")
    
    #Takes in the letter and checks if it matches the chosen word
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
        

    #Runs the game loop until user runs out of lives or until they guess the word
    def run_game(self):         
            while self.num_lives != 0:
                guess = input("Please enter your letter:")
                if len(guess) != 1 or not guess.isalpha():
                    print("Please, enter just one alphabetic character")
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
    game = Hangman(word_list, num_lives=5) #Number of lives can be changed here, enter any integer
    game.run_game()


if __name__ == '__main__':
    word_list = ['Banana', 'Apple', 'Orange', 'Peach', 'Pear'] #List of words can be changed here
    play_game(word_list)
