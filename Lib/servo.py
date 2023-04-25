import RPi.GPIO as GPIO
import time
from lcd import lcd_display

channel = (4,10)
servo = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(servo, GPIO.OUT)
p=GPIO.PWM(servo, 50)
p.start(3.1)

def opensimsim(tm):
    p.ChangeDutyCycle(8.2)
    lcd_display("Have a Good Day",2)
    time.sleep(tm)
    p.ChangeDutyCycle(3.1)

#try:
    #p.ChangeDutyCycle(8.2)
    #time.sleep(tm)
    #p.ChangeDutyCycle(3.1)
#except KeyboardInterrupt:
    #GPIO.cleanup()


def main():
    pass

if __name__ == "__main__":
    main()