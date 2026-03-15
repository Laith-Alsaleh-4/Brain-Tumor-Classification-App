import tensorflow as tf
import numpy as np
from PIL import Image

IMG_SIZE = (224, 224)

def preprocess_image(image, model_type="resnet"):
    image = image.resize(IMG_SIZE)
    image = np.array(image)

    if model_type == "resnet":
        image = tf.keras.applications.resnet50.preprocess_input(image)
    elif model_type == "efficientnet":
        image = tf.keras.applications.efficientnet.preprocess_input(image)
    else:
        image = image / 255.0

    image = np.expand_dims(image, axis=0)
    return image
