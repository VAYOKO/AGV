# Remote control Explora
# Kevin McAleer
# 17 March 2022

# We use Pygame to access the Xbox One Controller
#!/usr/bin/env python3
import serial
import pygame
import explorerhat
from time import sleep
from pygame.constants import JOYBUTTONDOWN
pygame.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

# Print out the name of the controller
print(pygame.joystick.Joystick(0).get_name())

# Xbox Joystick Axis:
# Axis 0 up down, down value is -1, up value is 1
# Axis 1 Left, Right, Left value is: -1, right value is 1
# center is always 0

# Main Loop


while True or KeyboardInterrupt:
  
    
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            if event.button == 0:
                print("button A down")
                
             

          
              
                
                
                
               
            if event.button == 1:
                print("button B down")
               
                
            if event.button == 2:
                print("button X down")
            if event.button == 3:
                print("button Y down")
            if event.button == 5:
                print("button RB down")
            if event.button == 6:
                print("button BK down")
            if event.button == 7:
                print("button ST down")
            if event.button == 8:
                print("button 8 down")
        if event.type == pygame.JOYAXISMOTION:
	    	
            if event.axis < 2: # Left stick
                if event.axis == 0: # left/right
                    if event.value < -0.5:
                        motor_speed = event.value * -1
                        print(f">> LEFT","motor_speed:",{motor_speed})
                       
                   

               
                    if event.value > 0.5:
                     
                       	motor_speed = event.value * 1
                        print(f">> RIGHT","motor_speed:",{motor_speed})
                        
                       
                if event.axis == 1: # up/down
                    if event.value < -0.5:
                       
                        motor_speed = event.value * -1
                        print(f">> UP","motor_speed:",{motor_speed})
                      
                      

                    if event.value > 0.5:
                     
                       	motor_speed = event.value * 1
                        print(f">> DOWN","motor_speed:",{motor_speed})
                      
             
