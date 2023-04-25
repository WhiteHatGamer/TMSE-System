import cv2
import os
import json


path = os.path.dirname(os.path.abspath(__file__)).replace("Lib","")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(path+r'\models\trainer.yml')
cascadePath = path+r"\models\face.xml"
with open(path+r"\reports\faces.json") as file:
    json_file = json.load(file)
faceCascade = cv2.CascadeClassifier(cascadePath)


def face_frame(frame):
    """
    To recognize face with trained model
    """
    offset = 10
    font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    if (faces == tuple()):
        return False
    for (x,y,w,h) in faces:
        face_id, perc = recognizer.predict(gray[y:y+h,x:x+w])
        perc = "%.2f" % perc
        rect_color = (face_id % 255,face_id % 205,face_id % 155)
        cv2.rectangle(frame,(x-offset,y-offset),(x+w+offset,y+h+offset),rect_color,3)
        try:
            face_id = json_file[str(face_id)]
        except:
            pass
        cv2.putText(frame,f'{perc}%', (x+h-50,y+h),font, 0.5, (0,255,0), thickness=2) #Draw the text
        cv2.rectangle(frame,(x-3,y-15),(x+w+3,y-15),rect_color,20)
        rect_color_inv = tuple(255-x for x in rect_color)
        cv2.putText(frame,f'{face_id}', (x-5,y-9),font, 0.6, rect_color_inv, thickness=2) #Draw the text
    return frame

def main():
    frame = cv2.imread(r"C:\Users\Thahir\Pictures\IMG_5338.JPG")
    face_frame(frame)
    pass

if __name__ == "__main__":
    main()