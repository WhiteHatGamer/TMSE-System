import cv2
from tensorflow.keras.preprocessing.image import array_to_img
img = cv2.imread('test.jpg')
img = cv2.resize(img, (405, 540))
cv2.imwrite('save0.jpg',img)
# create blob from image
blob = cv2.dnn.blobFromImage(image=img, scalefactor=0.01, size=(224, 224), mean=(104, 117, 123))
cv2.imwrite('save1.jpg',blob)
blobb = blob.reshape(blob.shape[2] * blob.shape[1],blob.shape[3],1)
cv2.imwrite('save2.jpg',blobb)
cv2.imshow('whg console',blobb)
