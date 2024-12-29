# write any code you want
from karel.stanfordkarel import *

def main():
    move()
    if front_is_clear():
        move()
        if front_is_clear():
            main()
        else:
            turn_left()
            turn_left()
    else:
        turn_left()
        turn_left()
    move()
