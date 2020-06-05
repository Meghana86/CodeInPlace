from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    # add your code here
    count = 0
    while front_is_clear():
        count = count + 1
        move()
    count = count + 1
    turn_left()
    turn_left()

    print(type(count))
    count1=int(count/2.0)
    print(type(count1))
    if count%2 == 0:
        for i in range(count1):
            move()
        put_beeper()
    else:
        count = count + 1
        for i in range(count1):
            move()
        put_beeper()

"""
    while front_is_clear():
        move()
    turn_left()
    turn_left()
"""

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
