import random


def select_random_word():
    word_list = ['Banana', 'Apple', 'Orange', 'Peach', 'Pear']
    word = str(random.choice(word_list))
    return word

def ask_for_input():
    while True:
        guess = input("Please enter your letter:")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            return guess
    
    
def check_guess(word, letter):
    letter_found = bool
    for i in list((word.lower())):
        if i == letter.lower():
            letter_found = True
        else:
            letter_found = False
    if letter_found == True:
        print("Good guess, the letter is correct!")
    else:
        print("Sorry the letter is wrong.")
    

word = select_random_word()
print("(Testing) word is " + word)


guess = ask_for_input()
check_guess(word, guess)

  
            