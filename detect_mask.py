# import the necessary packages
from imutils.video import VideoStream
from rtmask import detect_and_predict_mask
from tensorflow.keras.models import load_model
from colorama import init
import imutils
import time
import cv2
#for colour text for output
#init(autoreset=True)

#importable functions
#mask_video()

#[INFO]Commenting Codes are for Displayed Devices

def mask_video():
        # load pre-trained(best) face detector model
        prototxtPath = r"face_detector\deploy.prototxt"
        weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
        faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

        # load our face mask detector model
        maskNet = load_model("mask_detector.model")
        
        # assigning camera for video stream
        # print("\033[1;32m [INFO] starting video stream...")
        vs = VideoStream(src=0).start()
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
        # load pre-trained(best) face detector model
        prototxtPath = r"face_detector\deploy.prototxt"
        weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
        faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
        vidurl="".join(("http://",ip,':4747/video'))
        # load our face mask detector model
        maskNet = load_model("mask_detector.model")
        
        # assigning camera for video stream
        # print("\033[1;32m [INFO] starting video stream...")
        vs = VideoStream(src=vidurl).start()
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
