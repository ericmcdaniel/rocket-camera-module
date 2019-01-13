#!/bin/env python3
'''
**********************************************************************
* Filename    : rocket-camera-module.py
* Description : A script run by UW Fox Valley's Collegiate Rocketry
*               Competition (CRL) team, executed on a Raspberry Pi
*               fitted inside a high-powered rocket. This script
*               rotates a 3D-printed camera module, which takes linear
*               photos of the rocket's landing site. The photos get
*               stitched after the competition.
* Author      : Eric McDaniel - University of Wisconsin - Fox Valley
* E-mail      : MCDAE6861@students.uwc.edu
* Website     : https://github.com/McDanielES
* Version     : 1.1
* Update      : 4/03/18
**********************************************************************
'''
import sys
import RPi.GPIO as GPIO
import os
import picamera
from time import sleep

# Configure pulse-width modulation for servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
Servo = GPIO.PWM(18,50)

# Configuration for pull-up microswitch
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Configure camera library and relocate to output path
camera = picamera.PiCamera
os.chdir("/home/pi/rocket/New/Pictures")

# Delay start of photo capture to allow for rocket to land after launch
def InitialDelay():
	sleep(300)

	# One second start/stop to confirm the successful rotation of the servo motor
	Servo.start(99)
	sleep(1)
	Servo.stop()
	sleep(1)
	Servo.start(99)

# Reads the microswitch to see if module is currently in a position to take photos
def GetSwitchReading(RotatedServo, SwitchStatus):
	# Allows for the photo to be taken if servo has rotated and switch is depressed
	if RotatedServo and SwitchStatus == 0:
		return True
	return False

# Check if the module has advanced, allowing it to take new photos
def IsResetEligible(SwitchStatus):
	# Prevent taking extra photos without rotation occurs
	if SwitchStatus == 1:
		return True
	return False

def main():
	InitialDelay()		# Allow the rocket to land
	PicCounter = 0  	# Initialize photo counter
	nameCtr = 1			# Photo naming scheme
	RotatedServo = True # Initialize as ready to take a new photo
	while PicCounter < 16:
		# Read microswitch status from GPIO, where 0-Button pressed, 1-Not Pressed
		SwitchStatus = GPIO.input(17)

		# Calls method to reset eligibility, true only if module has rotated
		if not RotatedServo:
			RotatedServo = IsResetEligible(SwitchStatus)

		# Main conditional construct that takes action when all conditions are satisfied
		if GetSwitchReading(RotatedServo, SwitchStatus):
			
			# Stop the rotation and take a photo
			Servo.stop()
			sleep(0.1)	# Allows time for camera to be still
			with picamera.PiCamera() as camera:
				camera.capture("Image_%d.jpg" % nameCtr)
			
			# Increment the naming scheme/photo counter, reset conditions
			nameCtr += 1
			PicCounter += 1
			RotatedServo = False
			Servo.start(99)
		sleep(0.1)	

	# Turn off Pi after full iterations of loop
	from subprocess import call
	call("sudo poweroff", shell=True)

def destroy():
	GPIO.cleanup()

# Start Program with main
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy()