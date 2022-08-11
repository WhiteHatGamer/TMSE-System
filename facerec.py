from deepface import DeepFace
import cv2
img1 = DeepFace.detectFace('test2.jpg')
cv2.imshow('img1',img1)
print(end='\n')
verification = DeepFace.verify(img1_path = "test1.jpg",img2_path = "test2.jpg")
print( verfication)
