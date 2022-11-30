from lx16a import *
from moving_functions import *
import time


while True:
    walk_test = input("Enter time or steps: ")
    steps = input("Enter number of steps: ")
    speed = input("Enter speed: ")
    speed = int(speed)
    steps = int (steps)
    if(walk_test == "steps"):
        while (steps < 1 & speed < 50 ):
            steps = input("Enter number of steps: ")
            speed = input("Enter speed: ")
            speed = int(speed)
            steps = int (steps)
        move_step(steps= steps, speed= speed)
    if(walk_test == "time"):
        while (steps < 1 & speed < 50 ):
            steps = input("Enter number of steps: ")
            speed = input("Enter speed: ")
            speed = int(speed)
            steps = int (steps)
        move_time( endtime = steps, speed= speed)
    