import random


def select_random_word():
    word_list = ['Banana', 'Apple', 'Orange', 'Peach', 'Pear']
    word = str(random.choice(word_list))
    return word

def receive_and_check_letter():
    guess = input("Please enter your letter:")
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one alphabetic character!")
    else:
        print("Good guess!")


## Testing the functions
while True:   
    print(select_random_word())
    receive_and_check_letter()

  
            