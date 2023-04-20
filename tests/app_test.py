import RPi.GPIO as GPIO
import time

ledr = 7
ledo = 11
ledg = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(ledr, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(ledo, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ledg, GPIO.OUT,initial=GPIO.LOW)
temp=36
mask=0
try:
    while True:
        temp = int(input("Please Enter Temperatue:"))
        if temp < 36:
            GPIO.output(ledr,GPIO.LOW)
            GPIO.output(ledo,GPIO.HIGH)
            mask = int(input("Have Mask(0-NO 1-YES):"))
            if mask==1:
                print("Mask Detected. Have a Good Day")
                GPIO.output(ledo,GPIO.LOW)
                GPIO.output(ledg,GPIO.HIGH)
                time.sleep(3)
            elif mask==0:
                print("Please Put On Mask:You got 5 Secs..")
                for x in range(5,0,-1):
                    print (x)
                    time.sleep(1)
                mask = int(input("Have Mask(0-NO 1-YES):"))
                if mask==1:
                    print("ThankYou For Putting The Mask ON")
                    GPIO.output(ledo,GPIO.LOW)
                    GPIO.output(ledg,GPIO.HIGH)
                    time.sleep(3)
                elif mask==0:
                    print ("TIMES UP!!!")
                    GPIO.output(ledo,GPIO.LOW)
                    GPIO.output(ledr,GPIO.HIGH)
                    time.sleep(2)
        else:
            print("Tank You For Visiting Us.We have Informed The Authority.HAPPY QUARANTINE!!")
            GPIO.output(ledo,GPIO.LOW)
            GPIO.output(ledr,GPIO.HIGH)
            time.sleep(2)
        GPIO.output(ledg,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
