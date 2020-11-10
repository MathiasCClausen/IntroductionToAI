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
    
        mLeft.run_to_rel_pos(position_sp=240, speed_sp=400, stop_action="hold")
        mRight.run_to_rel_pos(position_sp=-100, speed_sp=150, stop_action="hold")
        sleep(1)
        
        break
        
        

def TurnLeft():
    
    while True:
        mLeft.run_to_rel_pos(position_sp=-100, speed_sp=150, stop_action="hold")
        mRight.run_to_rel_pos(position_sp=240, speed_sp=400, stop_action="hold")
        sleep(1)
        
        break
       

def TurnAround():
    while True:
        mLeft.run_to_rel_pos(position_sp=340, speed_sp=350, stop_action="hold")
        mRight.run_to_rel_pos(position_sp=-340, speed_sp=350, stop_action="hold")
        sleep(1)
        
        break
    
        

        
def GoOverFoward(): 
    while True: 
        mLeft.run_forever(speed_sp=350)
        mRight.run_forever(speed_sp=350)

        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=350)
            mRight.run_forever(speed_sp=350)

        if clLeft.value() > 40 or clRight.value() > 40:
            break


def GoOverBackward(): 
    while True: 
        mLeft.run_forever(speed_sp=-350)
        mRight.run_forever(speed_sp=-350)

        if clLeft.value() < 40 and clRight.value() < 40:
            mLeft.run_forever(speed_sp=-350)
            mRight.run_forever(speed_sp=-350)

        if clLeft.value() > 40 or clRight.value() > 40:
            break



# We have 4 directions, and initializes the "first" direction here. 
direction = 'up'

Commands = ['f','l','f','b','a','f','f','r']

def move(commands):
    
    for i in range(len(commands)):
            # The command up with the four different direction for the car.
            # Under here is the movement up.
        if(commands[i] == 'u' and direction == 'up'):
            GoOverFoward()
            FollowLine() 
        
        if(commands[i] == 'u' and direction == 'right'):
            TurnLeft()
            FollowLine() 
            direction = 'up'
        
        if(commands[i] == 'u' and direction == 'left'):
            TurnRight()
            FollowLine() 
            direction = 'up'
        
        if(commands[i] == 'u' and direction == 'down'):
            TurnAround()
            FollowLine() 
            direction = 'up'


        if(commands[i] == 'pf'):   
            PushCan()
                
                
            # For the command go down the map
        
        if(commands[i] == 'd' and direction == 'up'):
            mLeft.run_forever(speed_sp=0)
            mRight.run_forever(speed_sp=0)
                # SKAL TESTES!!
            GoOverBackward()
            sleep(1)
            BackWard()
            TurnAround()
            direction = 'down'
        
        if(commands[i] == 'd' and direction == 'right')
            TurnRight()
            FollowLine()
            direction = 'down'
        
        if(commands[i] == 'd' and direction == 'left')
            TurnLeft()
            FollowLine()
            direction = 'down'
        
        if(commands[i] == 'd' and direction == 'down')
            GoOverFoward()
            FollowLine()


            # For the commands go to the right in the map      
        
        if(commands[i] == 'r' and direction == 'up'):
            TurnRight()
            FollowLine()
            direction = 'right'
        
        if(commands[i] == 'r' and direction == 'right'):
            GoOverFoward()
            FollowLine()

        if(commands[i] == 'r' and direction == 'left'):
            TurnAround()
            FollowLine()
            direction = 'right'
        
        if(commands[i] == 'r' and direction == 'down'):
            TurnLeft()
            FollowLine()
            direction = 'right'

            # For the commands go left in the map
        if(commands[i] == 'l' and direction == 'up'):
            TurnLeft()
            FollowLine()
            direction = 'left'
        
        if(commands[i] == 'l' and direction == 'right'):
            TurnAround()
            FollowLine()
            direction = 'left'

        if(commands[i] == 'l' and direction == 'left'):
            GoOverFoward()
            FollowLine()
        
        if(commands[i] == 'l' and direction == 'down'):
            TurnRight()
            FollowLine()
            direction = 'left'

        
             


move(Commands)



# Turn off the motor and apply the brake
mLeft.stop(stop_action="brake")
mRight.stop(stop_action="brake") 
    

