import csv
import time
#import lcd to display

def csventry(student_id):
    f=open("data/entry.csv","a",newline='')
    writer = csv.writer(f)
    #student_id=str(input())
    curr = time.time()
    curr = time.ctime(float(curr))
    #Add code to display student code
    writer.writerow([student_id,curr])
    f.close()

def csvhightemp(student_id,temp):
    f=open("data/hightemp.csv","a",newline='')
    writer = csv.writer(f)
    #student_id=str(input())
    curr = time.time()
    curr = time.ctime(float(curr))
    #Add code to display student code
    writer.writerow([student_id,temp,curr])
    f.close()
