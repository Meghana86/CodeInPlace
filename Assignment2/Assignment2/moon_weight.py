"""
File: moon_weight.py
--------------------
Add your comments here.
"""


CNSTNT = 16.5/100
def main():
    weight_on_earth = int(input("Enter a weight on earth : "))
    weight_on_moon = weight_on_earth * CNSTNT
    print("Equivalent weight on moon : " + str(weight_on_moon))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
