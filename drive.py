#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep


# Initialize the motors.
# Highest value 900 and lowest value -900
mLeft = LargeMotor('outB')
mRight = LargeMotor('outC')

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
# In this mode the sensor will return a value between 0 and 100
# Sets the input lines
clRight = ColorSensor('in3')
clLeft = ColorSensor('in2')
clRight.mode='COL-REFLECT'
clLeft.mode='COL-REFLECT'

# Set the speed of the motors.
#mLeft.run_forever(speed_sp=250)
#mRight.run_forever(speed_sp=250)

# Function follow the line.
def FollowLine():
    while True:
        mLeft.run_forever(speed_sp=350)
        mRight.run_forever(speed_sp=350)

        if clLeft.value() < 40:
            mLeft.run_forever(speed_sp=0)
            mRight.run_forever(speed_sp=250)

        if clRight.value() < 40:
            mLeft.run_forever(speed_sp=250)
            mRight.run_forever(speed_sp=0) 
    
        if clLeft.value() < 40 and clRight.value() < 40:
            break 

def BackWard():
    while True:
        mLeft.run_forever(speed_sp=-250)
        mRight.run_forever(speed_sp=-250)

        if clLeft.value() < 40:
            mLeft.run_forever(speed_sp=-50)
            mRight.run_forever(speed_sp=-250)

        if clRight.value() < 40:
            mLeft.run_forever(speed_sp=-250)
            mRight.run_forever(speed_sp=-50)
        
        if clLeft.value() < 40 and clRight.value() < 40:
            break

def TurnRight():
    while True:
        mLeft.run_forever(speed_sp=350)
        mRight.run_forever(speed_sp=-100)
        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=350)
            mRight.run_forever(speed_sp=-100)
        if clLeft.value() > 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=350)
            mRight.run_forever(speed_sp=-100)
        
        if clLeft.value() > 40 and clRight.value() > 40:
            break

def TurnLeft():
    while True:
        mLeft.run_forever(speed_sp=-100)
        mRight.run_forever(speed_sp=350)

        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=-100)
            mRight.run_forever(speed_sp=350)

        if clLeft.value() < 40 and clRight.value() > 40:
            mLeft.run_forever(speed_sp=-100)
            mRight.run_forever(speed_sp=350)

        if clLeft.value() > 40 and clRight.value() > 40:
            break
        
        
def GoOverFoward(): 
    while True: 
        mLeft.run_forever(speed_sp=250)
        mRight.run_forever(speed_sp=250)


        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=250)
            mRight.run_forever(speed_sp=250)

        if clLeft.value() > 40 and clRight.value() > 40:
            break

def GoOverBackward(): 
    while True: 
        mLeft.run_forever(speed_sp=-250)
        mRight.run_forever(speed_sp=-250)

        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=-250)
            mRight.run_forever(speed_sp=-250)

        if clLeft.value() > 40 and clRight.value() > 40:
            break



FollowLine()
GoOverFoward()
FollowLine()
GoOverBackward()            
BackWard()
GoOverBackward()
BackWard()
GoOverFoward()
FollowLine()
GoOverFoward()
FollowLine()
GoOverBackward()
BackWard()
TurnRight()


# Turn off the motor and apply the brake
mLeft.stop(stop_action="brake")
mRight.stop(stop_action="brake") 
    

