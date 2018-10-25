import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin, GPIO.IN)
counter=1
time.sleep(4)
while counter<=4:
    if GPIO.input(pirPin):
        print("motion detected")
        os.system("fswebcam -F 4 --fps20 -r 800*600 /home/pi/priscilla")
        print("pic taken")
        time.sleep(1)
        counter = counter + 1
print("Testing")
exit()

 
