import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation 
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
import os 
import shutil
import random
import matplotlib.pyplot as plt
from IPython.display import Image
mobile = tf.keras.applications.mobilenet.MobileNet()

import os
os.chdir(r"C:\Users\yk406\Downloads")
def prepare_image(file):
    img_path = r'C:\Users\yk406\Downloads'
    img = image.load_img(img_path + file, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess.input(img_array_expanded_dims)

Image(filename='C:/Users/yk406/Downloads/1.jpg', width=450,height=300)
preprocessed_image = prepare_image('1.jpg')
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)
results 