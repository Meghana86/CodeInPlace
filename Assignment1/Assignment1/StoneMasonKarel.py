from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
"""
Karel will repair the quad in any world with a distance of 4 columns between any 2 columns of supporting arches 
"""

# pre : Karel should be facing east and at the left bottom corner position of the first column to be repaired
# post : Karel will be facing east and at the right bottom corner position of the repaired world
def main():
    while front_is_clear():
        repair_backtoposition()
        move_forward()
    repair_backtoposition()

# pre : Karel can be in any position
# post : Turn Karel 180 degree/ Karel is in reverse position
def turn_opposite():
    for i in range(2):
        turn_left()

# pre : Karel will be in bottom position of the supporting column and facing towards arch
# post : Place beepers if not present in the supporting columns
def repair_damage():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    if no_beepers_present():
        put_beeper()

# pre : Karel will be in bottom position of the supporting column
# post : Karel will be back to the position after repairing the supporting column
def repair_backtoposition():
    turn_left()
    repair_damage()
    turn_opposite()
    while front_is_clear():
        move()
    turn_left()

# pre : Karel will be in the bottom position of the supporting column facing east
# post : Move Karel by 4 positions so that Karel is present in the next supporting column that needs to be repaired
def move_forward():
    for j in range(4):
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
