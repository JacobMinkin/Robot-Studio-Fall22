from math import sin, cos
from lx16a import *
import time
import math
import numpy as np

LX16A.initialize('/dev/ttyUSB0')
def starting_position ():
    for index in range(0, 100):
        servo1.move(120)
        servo2.move(120) 
        time.sleep(0.05)

def move_leg_back ():
   t = 0
   front_pos = 120
   back_pos = 120
   while t < 90 :
    front_pos = 120 - 10 * math.sin(math.radians(t)) 
    back_pos  = 120 - 75 * math.sin(math.radians(t))
    servo1.move (front_pos )
    servo2.move ( back_pos )
    print(servo2.get_physical_angle())
    time.sleep(0.05)
    t += 1
   
def move_leg_forward ():
   t = 0
   front_pos_temp = servo1.get_physical_angle()
   back_pos_temp =  servo2.get_physical_angle()
   while t < 90 :
    front_pos = front_pos_temp + 10 * math.sin(math.radians(t)) 
    back_pos  = back_pos_temp + 10 * math.sin(math.radians(t))
    servo1.move (front_pos )
    servo2.move ( back_pos )
    print(servo2.get_physical_angle())
    time.sleep(0.05)
    t += 1

def move_leg (servo1_new, servo2_new):
   
    t = 0
    servo1_old = servo1.get_physical_angle()
    servo2_old =  servo2.get_physical_angle()
    print("Servo 1: " + str(servo2.get_physical_angle()) + " Servo 2: " + str(servo2.get_physical_angle()))
    t = 0
    servo1.move (servo1_new )
    servo2.move ( servo2_new )
    time.sleep(0.15)
    print("Servo 1: " + str(servo2.get_physical_angle()) + " Servo 2: " + str(servo2.get_physical_angle()))
"""     while t < 90 :
        print("Servo 1: " + str(servo2.get_physical_angle()) + " Servo 2: " + str(servo2.get_physical_angle()))
        
        servo1_final = servo1_old + (servo1_new - servo1_old) * math.sin(math.radians(t)) 
        servo2_final  = servo2_old + (servo2_new - servo2_old) * math.sin(math.radians(t))
        servo1.move (servo1_final )
        servo2.move ( servo2_final )
        time.sleep(0.05)
        t += 1 """
    

try:
    servo1 = LX16A(11)
    servo2 = LX16A(12)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
starting_position ()
move_leg_back ()
move_leg (120, 120)

