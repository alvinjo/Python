import RPi.GPIO as GPIO
import time

motionPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionPin, GPIO.IN)

def start():
    for i in range(100):
        time.sleep(2)
        if GPIO.input(motionPin):
            print (i,"motion detected")
        else:
            print(i,"nothing")

            
start()
GPIO.cleanup()
    
