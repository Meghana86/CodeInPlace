"""
File: nimm.py
-------------------------
Add your comments here.
"""
"""

def main():
    NO_OF_STONES=20
    player_no=1
    while NO_OF_STONES>0:
        print("There are "+ str(NO_OF_STONES) + " stones left")
        remove=int(input("Player "+ str(player_no)+" would you like to remove 1 or 2 stones? "))
        # print("Player "+ str(player_no)+" would you like to remove 1 or 2 stones? ")
        # remove=int(input("\n"))
        if remove == 1 or remove == 2:
            NO_OF_STONES = NO_OF_STONES - remove
        else:
            remove=int(input("Please enter 1 or 2: "))
            NO_OF_STONES = NO_OF_STONES - remove
        if player_no == 1:
            player_no=2
        else:
            player_no=1
        print("")
    print("Player "+str(player_no)+" wins!")

if __name__ == '__main__':
    main()
"""

def main():
    NO_OF_STONES=20
    player_no=1
    while NO_OF_STONES>0:
        print("There are "+ str(NO_OF_STONES) + " stones left")
        remove=int(input("Player "+ str(player_no)+" would you like to remove 1 or 2 stones? "))
        # print("Player "+ str(player_no)+" would you like to remove 1 or 2 stones? ")
        # remove=int(input("\n"))
        if remove == 1 or remove == 2:
            NO_OF_STONES = NO_OF_STONES - remove
        else:
            remove=int(input("Please enter 1 or 2: "))
            NO_OF_STONES = NO_OF_STONES - remove
        if player_no == 1:
            player_no=2
        else:
            player_no=1
        print("")
    print("Player "+str(player_no)+" wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
