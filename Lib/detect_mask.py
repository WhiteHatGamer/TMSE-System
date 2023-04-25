"""
This Module is for detecting mask from given cameraSource, ip or frame
"""
# import the necessary packages
from src.models.rtmask import detect_and_predict_mask
from tensorflow.keras.models import load_model
from keras import backend
from colorama import init
import imutils
import time
from Lib.recognize_face import face_frame
import cv2
import os


path = os.path.dirname(os.path.abspath(__file__)).replace("Lib","")
ct = time.time()
backend.clear_session()
maskNet = load_model(path+r"models\mask_detector.h5", compile=False)
# load pre-trained(best) face detector model
prototxtPath = r"models\deploy.prototxt"
weightsPath = r"models\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
ct = time.time() - ct
print(f"Took {ct:.2f}s for Loading face and mask model")
#for colour text for output
#init(autoreset=True)

#importable functions
#mask_video()

#[INFO]Commenting Codes are for Displayed Devices

def mask_video():
        """for normal built-in camera"""
        # assigning camera for video stream
        # print("\033[1;32m [INFO] starting video stream...")
        vs = cv2.VideoCapture(0)
        summ = red = 0
        c=cn=cm=1
        dmask=nmask=0
        # loop over the frames from the video stream here for 2 sec
        t_end = time.time() + 2
        while time.time() < t_end:
                # grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
                frame = vs.read()
                frame = imutils.resize(frame, width=400)
                c+=1
                # detect faces in the frame and determine if they are wearing a face mask or not
                (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)
                
                #box = locs[0]
                #(startX, startY, endX, endY) = box
                #pred = preds[0]
                #(mask, withoutMask) = pred
                #summ = (summ+1) if mask > withoutMask else summ
                # loop over the detected face locations and their corresponding locations
                for (box, pred) in zip(locs, preds):
                         #unpack the bounding box and predictions
                        (startX, startY, endX, endY) = box
                        (mask, withoutMask) = pred
                        # determine the class label and color we'll use to draw the bounding box and text
                        #label = "Mask" if mask > withoutMask else "No Mask"
                        if mask > withoutMask:
                                summ = (summ+1)
                                dmask+=mask
                                cm+=1
                        else:
                                nmask+=withoutMask
                                cn+=1
                                summ = summ
                        #color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        
                        # include the probability in the label
                        #label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
        
                        # uncomment to display the label and bounding box rectangle on the output
                        # frame
                        #cv2.putText(frame, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                        #cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
                # show the output frame
                #cv2.imshow("Frame", frame)
                #key = cv2.waitKey(1) & 0xFF
                # exit from the loop by pressing key q
                #if key == ord("q"):
                        #break
        
        # releasing every windows captured
        cv2.destroyAllWindows()
        vs.stop()
        if summ/c > 0.55:
                red = 1
                mask = dmask/cm
        else:
                red = 0
                mask = nmask/cn
        
        return red,mask

def mask_ipvideo(ip):
        """for ip camera"""
        vidurl="".join(("http://",ip,':4747/video'))
        # assigning camera for video stream
        # print("\033[1;32m [INFO] starting video stream...")
        vs = cv2.VideoCapture(vidurl)
        summ = red = 0
        c=1
        dmask=nmask=cm=cn=0
        # loop over the frames from the video stream here for 2 sec
        t_end = time.time() + 2
        while time.time() < t_end:
                # grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
                frame = vs.read()
                frame = imutils.resize(frame, width=400)
                c+=1
                # detect faces in the frame and determine if they are wearing a face mask or not
                (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)
                
                #box = locs[0]
                #(startX, startY, endX, endY) = box
                #pred = preds[0]
                #(mask, withoutMask) = pred
                #summ = (summ+1) if mask > withoutMask else summ
                # loop over the detected face locations and their corresponding locations
                for (box, pred) in zip(locs, preds):
                         #unpack the bounding box and predictions
                        (startX, startY, endX, endY) = box
                        (mask, withoutMask) = pred
                        # determine the class label and color we'll use to draw the bounding box and text
                        label = "Mask" if mask > withoutMask else "No Mask"
                        if mask > withoutMask:
                                summ = (summ+1)
                                dmask+=mask
                                cm+=1
                        else:
                                nmask+=withoutMask
                                cn+=1
                                summ = summ
                        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        
                        # include the probability in the label
                        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
        
                        # uncomment to display the label and bounding box rectangle on the output
                        # frame
                        cv2.putText(frame, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
                # show the output frame
                cv2.imshow("Frame", frame)
                #key = cv2.waitKey(1) & 0xFF
                # exit from the loop by pressing key q
                #if key == ord("q"):
                        #break
        
        # releasing every windows captured
        cv2.destroyAllWindows()
        vs.stop()
        if summ/c > 0.55:
                red = 1
                mask = dmask/cm
        else:
                red = 0
                mask = nmask/cn
        
        return red,mask


def mask_frame(frame):
        """
        Detecting if theres Mask in a given Frame
        """
        # grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
        #frame = imutils.resize(frame, width=400)

        # detect faces in the frame and determine if they are wearing a face mask or not
        try:
                ct = time.time()
                (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)
                ct = time.time() - ct
                print(f"Took {ct:.2f}s for detecting face and mask")
        except:
                return frame
        
        # loop over the detected face locations and their corresponding locations
        for (box, pred) in zip(locs, preds):
                 #unpack the bounding box and predictions
                (startX, startY, endX, endY) = box
                (mask, withoutMask) = pred
                # determine the class label and color we'll use to draw the bounding box and text
                label = "Mask" if mask > withoutMask else "No Mask"
                color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

                # include the probability in the label
                label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
                
                cv2.putText(frame, label, (startX-10, endY+25),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                if "No Mask" in label:
                        ct = time.time()
                        face_res = face_frame(frame)
                        ct = time.time() - ct
                        print(f"Took {ct:.2f}s for recognizing face")
                        try:
                                if not face_res:
                                        pass
                        except:
                                return face_res
                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
        # show the output frame
        return frame

def main():
    pass

if __name__ == "__main__":
    main()