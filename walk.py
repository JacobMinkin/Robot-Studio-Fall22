from lx16a import *
from moving_functions import *


while True:
    speed = input("Enter speed: ")
    if(speed == "test"):
        new_move_time()
    if(speed == "exit"):
        quit()
    walk_test = input("Enter time, steps or turn: ")
    if(walk_test == "steps"):
        steps = input("Enter number of steps: ")
        speed = int(speed)
        steps = int (steps)
        move_step(steps= steps, speed= speed)
    elif (walk_test == "time"):
        time_num = input("Enter time in seconds: ")
        speed    = int(speed)
        time_num = int (time_num)
        move_time( endtime = time_num, speed= speed)
    elif(walk_test == "turn"):
        side  = input("Enter direction of turn (right or left): ")
        steps = input("Enter number of steps: ")
        speed = int(speed)
        steps = int (steps)
        move_turn(steps= steps, speed= speed, side= side)
    else:
        exit()