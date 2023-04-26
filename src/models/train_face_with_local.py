#Copyright Anirban Kar (anirbankar21@gmail.com)
#
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

import cv2,os
import numpy as np
from PIL import Image 
import json

path = os.path.dirname(os.path.abspath(__file__)).replace('\src\models',"")
faceCascade = cv2.CascadeClassifier(path+r'\models\face.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
dataPath = path+r'\data\preprocessed'
with open(path+r"\reports\faces.json") as file:
    json_file = json.load(file)

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
            if face_id not in json_file.keys():
                print("###id name not enrolled###")
                name = input("Enter Your Name: ")
                json_file.update({face_id:name})
                with open(f"{path}/reports/faces.json",'w') as file:
                    json.dump(json_file, file, indent=4)
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
