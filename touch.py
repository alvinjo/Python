import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

def start():
    while True:
        try:
            if (GPIO.input(PIR_PIN)==True):
                print ("pressed")
         except KeyboardInterrupt:
             break

start()
GPIO.cleanup()
