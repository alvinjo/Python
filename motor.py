import sys
import RPi.GPIO as GPIO
import time

switchA = 18
switchB = 17
out1 = 24
out2 = 23
ena = 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(switchA, GPIO.IN)
GPIO.setup(switchB, GPIO.IN)
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

GPIO.output(out1, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

GPIO.setup(switchA, GPIO.IN)
GPIO.setup(switchB, GPIO.IN)
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

GPIO.output(out1, GPIO.LOW)
GPIO.output(out2, GPIO.LOW)
GPIO.output(ena, GPIO.HIGH)

def forward():
        print("forward")
        GPIO.output(out1, GPIO.HIGH)
        GPIO.output(out2, GPIO.LOW)
        x='z'

def backward():
        print("backward")
        GPIO.output(out1, GPIO.LOW)
        GPIO.output(out2, GPIO.HIGH)
        x='z'

def stop():
        GPIO.output(out1, GPIO.LOW)
        GPIO.output(out2, GPIO.LOW)
        x='z'

def topPos():
        while GPIO.input(switchA) == True:
                backward()
        stop()
        print("back to starting position")

def downPos():
        while GPIO.input(switchB) == True:
                forward()
 	stop()
        print("in feeding position")

def feed():
        if GPIO.input(switchA) == True:
                topPos()
        time.sleep(3.0)
        downPos()
        forward()
        time.sleep(6.0)
        stop()
        time.sleep(3.0)
        #in feeding pos, ready to move
        forward()
        time.sleep(3.0)
        backward()
        time.sleep(3.0)
	stop()
        time.sleep(3.0)
        #jigging performed
        topPos()

arguments = False

if len(sys.argv) > 1:
        arguments = True
        if str(sys.argv[1]) == "feed":
                feed()
        elif str(sys.argv[1]) == "top":
                topPos()
        elif str(sys.argv[1]) == "f":
                forward()
        elif str(sys.argv[1]) == "b":
                backward()
        elif str(sys.argv[1]) == "s":
                stop()

while(arguments == False):
        print("CONTROLS: forward(f), backward(b), stop(s), exit(e), feeding mod$
        x = raw_input()

        if x=='f':
                forward()

        elif x=='b':
                backward()

        elif x=='s':
                stop()

        elif x=='e':
                print("exit")
                stop()
                GPIO.cleanup()
                break

        elif x=='tfeed':
                print("timed feeding")
                forward()
                time.sleep(15.0)
                stop()
                time.sleep(3.0)
                backward()
                time.sleep(15.0)
                stop()

        elif x=='feed':
                print("feeding")
                feed()

        elif x=='top':
                print("reset to start position")
                topPos()

        elif x=='down':
                print("moving to feed position")

        else:
                print("wrong input")
























