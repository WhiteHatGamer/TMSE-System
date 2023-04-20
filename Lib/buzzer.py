import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzzer=29
GPIO.setup(buzzer,GPIO.OUT)

def buzz(tm,dly):
    for i in range(tm):
        GPIO.output(buzzer,GPIO.HIGH)
        time.sleep(dly)
        GPIO.output(buzzer,GPIO.low)
        time.sleep(0.1)
        
def buzzlong(tm):
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(tm)
    GPIO.output(buzzer,GPIO.LOW)
