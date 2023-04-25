"""
This is to run on pc with limited features like:
# mask Detection
"""

#from Lib.talkback import TTstudnm, TTstr, playsn
#from Lib.studentdb import findnm
from Lib.detect_mask import mask_frame
#import Lib.telegrambot as telegrambot
import cv2
import time


video_stream = cv2.VideoCapture(0)
while True:
    if not video_stream.isOpened():
        continue
    #Get a frame
    ret, frame = video_stream.read()

    #check if theres mask
    frame = mask_frame(frame)
    #show the frame
    cv2.imshow("Video",frame)
    k = cv2.waitKey(1)
    if k == 27:    
        cv2.putText(frame,"Exiting . . .",(0,250),cv2.FONT_HERSHEY_SIMPLEX,3.0,(0,0,255),thickness=10)
        cv2.imshow("Video",frame)
        cv2.waitKey(1)
        time.sleep(2)
        cv2.destroyAllWindows()        
        break