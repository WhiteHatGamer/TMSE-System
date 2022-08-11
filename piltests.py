import PIL
import os
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import UnidentifiedImageError
DIRECTORY = r"C:\Users\WHG-PC\Desktop\cs18\Test Folder\dataset"
CATEGORIES = ["with_mask", "without_mask"]

# storing the list of images in our dataset directory, then appending all as arrays and class images
#\033[1;32m for colour change
print(" [INFO] Loading Images...")

data = []
labels = []
for category in CATEGORIES:
    path = os.path.join(DIRECTORY, category)
    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        try:
            image = load_img(img_path, target_size=(224, 224))
        except PIL.UnidentifiedImageError:
            continue
        data.append(image)
        labels.append(category)
