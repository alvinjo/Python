import sys
import RPi.GPIO as GPIO
import time
import threading

switchOn = 18
outFan = 17
outGlowplug = 23
outPumpWater = 24
outPumpFuel = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchOn, GPIO.IN)
GPIO.setup(outFan, GPIO.OUT)
GPIO.setup(outGlowplug, GPIO.OUT)
GPIO.setup(outPumpWater, GPIO.OUT)
GPIO.setup(outPumpFuel, GPIO.OUT)

GPIO.output(outFan, GPIO.LOW)
GPIO.output(outGlowplug, GPIO.LOW)
GPIO.output(outPumpWater, GPIO.LOW)
GPIO.output(outPumpFuel, GPIO.LOW)

def startGlowplug(arg1, stop_event):
    while not stop_event.is_set():
        GPIO.output(outGlowplug, GPIO.HIGH)
        time.sleep(180.0)
        GPIO.output(outGlowplug, GPIO.LOW)    

def pumpFuelPulse(arg1, stop_event):
    while not stop_event.is_set():
        GPIO.output(outPumpFuel, GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(outPumpFuel, GPIO.LOW)
        time.sleep(1.0)
    #speed up to 2 pulse per second

glowplug_stop = threading.Event()
glowplugThread = threading.Thread(target=startGlowplug, args=(1, glowplug_stop))

pumpfuel_stop = threading.Event()
pumpFuelThread = threading.Thread(target=pumpFuelPulse, args=(1, pumpfuel_stop))

def start():
    print("ON")
    #start fan
    GPIO.output(outFan, GPIO.HIGH)
    #start pumpwater
    GPIO.output(outPumpWater, GPIO.HIGH)
    #after 5s, start glowplug thread
    time.sleep(5.0)
    glowplugThread.start()
    #after 1minute, start pumpFuel thread 
    time.sleep(55.0)
    pumpFuelThread.start()
                  

def stop():
    #stop fan
    GPIO.output(outFan, GPIO.LOW)
    #stop glowplug thread
    glowplug_stop.set()
    #stop pumpfuel thread
    pumpfuel_stop.set()
    #stop pumpwater
    stopWater()

def stopWater():
    time.sleep(120)
    GPIO.output(outPumpWater, GPIO.LOW)


 
def tempMonitor():
    temperature = 0;
    while(True):
        if(temperature >= 80):
            stop()


lastCommand = ""
while(True):
    print("CONTROLS: start, stop, end")
    option = input("")

    if option=="start":
        if(lastCommand==option):
            print("Program already started. Call 'stop' before starting again.")
        else:    
            lastCommand = option
            start()
    elif option=="stop":
        if(lastCommand==option):
            print("Program already stopped.")
        elif(lastCommand==""):
            print("Program not started. Call 'start' before stopping.")
        else:
            lastCommand==option
            stop()
    elif option=="end":
        if(lastCommand=="start"):
            stop()
        GPIO.cleanup()
        break
    
    print("\n")
        

    
