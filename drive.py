#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep




# Initialize the motors.
# Highest value 900 and lowest value -900
mLeft = LargeMotor('outB')
mRight = LargeMotor('outC')

#robot = DriveBase(mLeft, mRight, wheel_diameter=55.5, axle_track=120)

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
        mLeft.run_forever(speed_sp=450)
        mRight.run_forever(speed_sp=450)

        if clLeft.value() < 40:
            mLeft.run_forever(speed_sp=000)
            mRight.run_forever(speed_sp=250)

        if clRight.value() < 40:
            mLeft.run_forever(speed_sp=250)
            mRight.run_forever(speed_sp=000) 
    
        if clLeft.value() < 40 and clRight.value() < 40:
            break 

def PushCan():
    while True:
        mLeft.run_forever(speed_sp=350)
        mRight.run_forever(speed_sp=350)

        if clLeft.value() < 40:
            mLeft.run_forever(speed_sp=00)
            mRight.run_forever(speed_sp=250)

        if clRight.value() < 40:
            mLeft.run_forever(speed_sp=250)
            mRight.run_forever(speed_sp=00) 
    
        if clLeft.value() < 40 and clRight.value() < 40:
            break


def BackWard():
    while True:
        mLeft.run_forever(speed_sp=-350)
        mRight.run_forever(speed_sp=-350)
        
        if clLeft.value() < 40 and clRight.value() < 40:
            break

def TurnRight():
    while True:
    
        mLeft.run_to_rel_pos(position_sp=180, speed_sp=400, stop_action="hold")
        mRight.run_to_rel_pos(position_sp=-180, speed_sp=250, stop_action="hold")
        sleep(1)
        
        break
        
        

def TurnLeft():
    
    while True:
        mLeft.run_to_rel_pos(position_sp=-180, speed_sp=250, stop_action="hold")
        mRight.run_to_rel_pos(position_sp=180, speed_sp=400, stop_action="hold")
        sleep(1)
        
        break
       

def TurnAround():
    while True:
        mLeft.run_to_rel_pos(position_sp=380, speed_sp=350, stop_action="hold")
        mRight.run_to_rel_pos(position_sp=-380, speed_sp=350, stop_action="hold")
        sleep(1)
        
        break
    
        

        
def GoOverFoward(): 
    while True: 
        mLeft.run_forever(speed_sp=350)
        mRight.run_forever(speed_sp=350)

        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=350)
            mRight.run_forever(speed_sp=350)

        if clLeft.value() > 40 and clRight.value() > 40:
            break

def GoOverBackward(): 
    while True: 
        mLeft.run_forever(speed_sp=-350)
        mRight.run_forever(speed_sp=-350)

        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=-350)
            mRight.run_forever(speed_sp=-350)

        if clLeft.value() > 40 and clRight.value() > 40:
            break



Commands = ['f','f','pf','b','r','f','l','f','l','f','f','p','b','a']

def move(commands):
    
    for i in range(len(commands)):
        if(commands[i] == 'f'):
            FollowLine() 
            GoOverFoward()
                
        if(commands[i] == 'pf'):   
            PushCan()
                
                

        if(commands[i] == 'b'):
            mLeft.run_forever(speed_sp=0)
            mRight.run_forever(speed_sp=0)
            
            GoOverBackward()
            sleep(1)
            BackWard()
                
                
        if(commands[i] == 'r'):
            TurnRight()
            
        if(commands[i] == 'l'):
            TurnLeft()

        if(commands[i] == 'a'):
            TurnAround()
             


move(Commands)



# Turn off the motor and apply the brake
mLeft.stop(stop_action="brake")
mRight.stop(stop_action="brake") 
    

