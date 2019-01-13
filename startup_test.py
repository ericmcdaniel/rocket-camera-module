#!/bin/env python3
import sys
#import RPi.GPIO as GPIO
import os
#import picamera
from time import sleep
'''
# Configure pulse-width modulation for servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
Servo = GPIO.PWM(18,50)

# Configure pull-up microswitch
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configure camera library and output path
camera = picamera.PiCamera
os.chdir("/home/pi/rocket/New/Pictures")
'''
# Programmer-Defined Functions
def InitialDelay():
	# Length to be changed to match the length of the flight
    sleep(2)
    print("Delay successful")
'''
	# One second start/stop to confirm the rotation of the servo motor
    Servo.start(99)
    sleep(1)
    Servo.stop()
    sleep(1)
    Servo.start(99)
'''


def GetSwitchReading(RotatedServo, SwitchStatus):
	# Allows for the photo to be taken if servo has rotated and switch is depressed
	if (RotatedServo) and (SwitchStatus == 0):
		print("true")
		return True
	return False        

def IsResetEligible(SwitchStatus):
	# Resets the ability to take a new photo if the servo has rotated
	if (SwitchStatus == 1):
		print("Successful reset.")
		return True
	return False

def main():
	InitialDelay()
	PicCounter = 0  	# Initialize photo counter
	d = 1       		# Photo naming scheme
	RotatedServo = True # Initialize as ready to take a new photo
	while PicCounter < 16:
		#SwitchStatus = GPIO.input(17) # 0-Button pressed, 1-Not Pressed
		SwitchStatus = int(input("Input status (0-Button pressed, 1-Not Pressed): "))
		# Calls method to reset eligibility
		if (RotatedServo == False):
			RotatedServo = IsResetEligible(SwitchStatus)

		# Main conditional construct that takes action when all conditions are satisfied
		if GetSwitchReading(RotatedServo, SwitchStatus) == True:
			#Servo.stop()
			sleep(0.1)    # Allows time for camera to be still        
			#with picamera.PiCamera() as camera:
			#   camera.capture("Image_%d.jpg" % d)
			print("picture taken")
			# Increment the naming scheme/photo counter, reset conditions
			d += 1
			PicCounter += 1
			RotatedServo = False
			#Servo.start(99)
		sleep(0.1)	
     
	# Turn off Pi after full iterations of loop	      
	from subprocess import call
	call("sudo poweroff", shell=True)
    
#Start Program with Main
main()
