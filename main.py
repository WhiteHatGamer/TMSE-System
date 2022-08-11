import RPi.GPIO as GPIO
import time
from lcd import lcd_display
from talkback import TTstudnm
from talkback import TTstr
from talkback import playsn
import studentdb
from temperature import read_temp
from detect_mask import mask_video
import telegrambot
import buzzer
import entry
import servo

ledg = 31
ledo = 32
ledr = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(ledr, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(ledo, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ledg, GPIO.OUT,initial=GPIO.LOW)
temp=36
mask=0

try:
    while True:
        playsn("idscan")
        lcd_display("TMSE System",1)
        lcd_display("Please Scan ID",2)
        student_id=str(input())
        student_name,student_univ = findnm(student_id)
        if(student_name==student_id):
            telegrambot.sendnostud(student_id)
        TTstudnm(student_name)
        lcd_display(student_name,1)
        lcd_display(student_univ,2)
        time.sleep(1)
        lcd_display("Place Finger on",1)
        playsn("tempscan")
        lcd_display("Temperature sensor",2)
        tempc,tempf = read_temp()
        lcd_display("Temperature Read",1)
        lcd_display(''.join("C: ",tempc," ,F: ",tempf),2)
        if tempc < 36:
            playsn("templow")
            GPIO.output(ledr,GPIO.LOW)
            GPIO.output(ledo,GPIO.HIGH)
            lcd_display("TMSE System",1)
            lcd_display("Please Scan Mask",2)
            mask,perc = mask_video()
            if mask==1:
                lcd_display("Mask Detected",1)
                playsn("maskyes")
                lcd_display(''.join(perc,"%"),2)
                GPIO.output(ledo,GPIO.LOW)
                GPIO.output(ledg,GPIO.HIGH)
                servo.opensimsim(5)
                entry.csventry(student_id)
                time.sleep(1.5)
            elif mask==0:
                lcd_display("Please Put On Mask",2)
                playsn("maskno1")
                lcd_display("You got 5 Secs..",1)
                time.sleep(1)
                for x in range(5,0,-1):
                    lcd_display(''.join(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),2)
                    GPIO.output(ledr,GPIO.HIGH)
                    buzzer.buzz(1,0.9)
                    GPIO.output(ledr,GPIO.LOW)
                mask,perc = mask_video()
                if mask==1:
                    lcd_display("Mask Detected",1)
                    playsn("maskyes")
                    lcd_display(''.join(perc,"%"),2)
                    GPIO.output(ledo,GPIO.LOW)
                    GPIO.output(ledg,GPIO.HIGH)
                    servo.opensimsim(5)
                    entry.csventry(student_id)
                    time.sleep(1.5)
                elif mask==0:
                    lcd_display("TMSE System",1)
                    lcd_display("TIMES UP!!!",2)
                    GPIO.output(ledo,GPIO.LOW)
                    playsn("maskno2")
                    GPIO.output(ledr,GPIO.HIGH)
                    telegrambot.sendnnm(student_id,student_name)
                    buzzer.long(3)
                else:
                    pass
        else:
            playsn("temphigh")
            lcd_display("Temperature HIGH",1)
            GPIO.output(ledr,GPIO.HIGH)
            telegrambot.sendht(student_id,student_name)
            entry.csvhightemp(student_id,''.join("C: ",tempc," ,F: ",tempf))
            buzzer.buzz(5,1)
            time.sleep(1.5)
        GPIO.output(ledg,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
