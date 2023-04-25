#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import cv2
import os
import json
import numpy as np
from PIL import Image 

path = os.path.dirname(os.path.abspath(__file__)).replace('\src\models',"")

cam = cv2.VideoCapture(0)
with open(path+r"\reports\faces.json") as file:
    json_file = json.load(file)
dataPath = path+r'\data\preprocessed'
faceCascade = cv2.CascadeClassifier(path+r'\models\face.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
i=0
offset=50
id = input('Enter your id: ')
if id in json_file.keys():
    choice = input("id already enrolled. want to Overwrite? (Y/N): ")
    if choice.lower() not in ['y','yes']:
        print("Exiting . . .")
        exit()
name = input("Enter Your Name: ")
try:
    os.mkdir(f"{dataPath}/{id}")
except:
    pass
while True:
    ret, frame =cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite(f"{dataPath}/{id}/face-.{str(i)}.jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(frame,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('Video Feed',frame[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(1)
    if i>20:
        print("Added one Face to DataBase")
        json_file.update({id:name})
        with open(f"{path}/reports/faces.json",'w') as file:
            json.dump(json_file, file, indent=4)
        cam.release()
        cv2.destroyAllWindows()
        break

def get_images_and_labels(datapath):
    images_paths = [ f.path for f in os.scandir(datapath) if f.is_dir() ]

    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for images_path in images_paths:
        image_path = [os.path.join(images_path, f) for f in os.listdir(images_path)]
        for image in image_path:
            # Get the label of the image
            face_id = int(os.path.basename(os.path.dirname(image)))
            print(face_id)
            # Read the image and convert to grayscale
            image_pil = Image.open(image).convert('L')
            # Convert the image format into numpy array
            image = np.array(image_pil, 'uint8')
            # Detect the face in the image
            faces = faceCascade.detectMultiScale(image)
            # If face is detected, append the face to images and the label to labels
            for (x, y, w, h) in faces:
                images.append(image[y: y + h, x: x + w])
                labels.append(face_id)
                cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                cv2.waitKey(1)
    # return the images list and labels list
    return images, labels


images, labels = get_images_and_labels(dataPath)
cv2.imshow('test',images[0])
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.save(path+r'\models\trainer.yml')
cv2.destroyAllWindows()
