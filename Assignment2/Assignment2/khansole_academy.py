"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random
"""
import random

CNT=3
def main():
    generate_num(1)

def generate_num(count):
    num1=random.randint(10,99)
    num2=random.randint(10,99)
    total=num1+num2
    # user_output=int(input("What is "+str(num1)+" + "+str(num2)+" ? "))
    # print("Your answer : " + str(user_output))
    print("What is "+str(num1)+" + "+str(num2)+" ? ")
    user_output=int(input("Your answer : "))
    if total == user_output:
        print("Correct! You've gotten " + str(count) + " correct in a row")
        if count == CNT:
            print("Congratulations! You mastered addition.")
            # again=input("Would u like to  try again?")
            # if again == 'yes':
            #    main()
        else:
            count=count+1
            generate_num(count)
    else:
        print("Incorrect. The expected answer is "+str(total))
        count=1
        generate_num(1)
     
if __name__ == '__main__':
    main()
"""
CNT=3
def main():
    generate_num(1)

def generate_num(count):
    num1=random.randint(10,99)
    num2=random.randint(10,99)
    total=num1+num2
    print("What is "+str(num1)+" + "+str(num2)+" ? ")
    user_output=int(input("Your answer : "))
    if total == user_output:
        print("Correct! You've gotten " + str(count) + " correct in a row")
        if count == CNT:
            print("Congratulations! You mastered addition.")
            # again=input("Would u like to  try again?")
            # if again == 'yes':
            #    main()
        else:
            count=count+1
            generate_num(count)
    else:
        print("Incorrect. The expected answer is "+str(total))
        count=1
        generate_num(1)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
