from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""

"""
Karel paints 3 exterior sides of each in a world of three buildings 
"""

def main():
    for i in range(3):  # Paints 3 buildings in a given world
        for j in range(2):  # Paints 2 sides of a building
            paint()
            move()
        paint()  # Paints 3rd side of a building
        turn_left()
        turn_left()
    turn_left()

# pre : Karel will be facing left
# post : Karel need to turn right from the the current position
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# pre : Karel is in the top right corner of the building (external)
# post : Karel paints one side of the building
def paint():
    turn_left()
    while front_is_blocked():
        put_beeper()
        turn_right()
        move()
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
