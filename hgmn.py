import random


word_list=['wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired']
#getting random words
def get_word():
    word=random.choice(word_list)
    return word.upper()


def play(word):
    word_completion="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words =[]
    tries = 6 
    print("welcome!.Lets play hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries >0:
        guess = input("please guess a letter").upper()
        if len(guess) ==1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already enterrd that letter", guess)
            elif guess not in word :
                print(guess,"sorry no match of letter")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("you made that letter",guess ,"is in word")
                guessed_letters.append(guess)
                word_as_list =list(word_completion)
                indices =[i for i ,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion="".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True

                
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the letters",guess)
            elif guess !=word:
                print(guess,"is not in word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed =True
                word_completion =word
        else:
            print("not valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    guessed = True
    if guessed:
        print("congrats you guessed coreectly")

    else:
        print("better luck next time.you ran out of tries")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word=get_word()
    play(word) 

    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()





