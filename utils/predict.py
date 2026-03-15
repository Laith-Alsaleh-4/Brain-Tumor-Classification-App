import tensorflow as tf
import numpy as np

def load_model(path):
    return tf.keras.models.load_model(path)

def predict(model, img_tensor):
    probs = model.predict(img_tensor)[0]
    class_index = np.argmax(probs)
    confidence = probs[class_index]
    labels = ["Glioma", "Meningioma", "No Tumor", "Pituitary Tumor"]

    return {
        "label": labels[class_index],
        "confidence": float(confidence),
        "probs": probs
    }
