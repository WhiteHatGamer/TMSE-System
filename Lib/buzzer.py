import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzzer=29
GPIO.setup(buzzer,GPIO.OUT)

def buzz(tm,dly):
    """buzz the buzzer for *tm* time/s with *dly*sec delay in between"""
    for i in range(tm):
        GPIO.output(buzzer,GPIO.HIGH)
        time.sleep(dly)
        GPIO.output(buzzer,GPIO.low)
        time.sleep(0.1)
        
def buzzlong(tm):
    """buzz the buzzer for *tm* time/s long without break"""
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(tm)
    GPIO.output(buzzer,GPIO.LOW)


def main():
    pass

if __name__ == "__main__":
    main()