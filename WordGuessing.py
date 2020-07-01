"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    word=secret_word
    hidden='-'
    inp=''
    no_guesses = 8
    list_word=list(word)
    
    for i in range(len(word)-1):
        hidden=hidden+'-'
    hidden_word=list(hidden)
    #print('Hidden',hidden,hidden_word)

    while no_guesses <= 8 :
        # print(type(word))
        print("The word now looks like this: ",hidden_word)
        print("\n You have "+str(no_guesses)+" left")
        inp=input("Type a single letter here, then press enter: ")
        for i in range(len(word)):
            if list_word[i]==inp:
                hidden_word[i]=inp
                # print('i=',i)
            elif list_word[i]=='-':
                hidden_word[i]=str('-')
                print('i=',i)
            else :
                hidden_word[i]=hidden_word[i]
            # print(hidden_word)
        #print("\n You have "+str(no_guesses)+" left")
        #inp=input("Type a single letter here, then press enter: ")

        if inp not in word:
            no_guesses = no_guesses - 1

        if list_word == hidden_word:
            print("Matches")
            break

        if no_guesses == 0:
            print("You have reached the maximum attempts")
            break


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    print(index)
    if index == 0:
        return 'HAPPIE'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    print(secret_word)
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
