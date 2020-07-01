def main():
    word='HAPPY'
    hidden='-'
    inp=''
    no_guesses=8
    list_word=list(word)
    # hidden_word=list(hidden)
    print(list_word)

    for i in range(len(word)-1):
        hidden=hidden+'-'
    hidden_word=list(hidden)
    #print('Hidden',hidden,hidden_word)

    while no_guesses <= 8 :
        # print(type(word))
        print("The word now looks like this: ",hidden_word)
        print('.'.join(str(char) for char in hidden_word)
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

if __name__ == '__main__':
    main()
