# utils/gradcam.py
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.cm as cm

data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.05),
    keras.layers.RandomZoom(0.05),
], name="data_augmentation")

def make_gradcam_heatmap(img_array, base_model, classifier_model, last_conv_layer_name="conv5_block3_out", pred_index=None):
    """
    Generate Grad-CAM heatmap for a single image.
    """
    last_conv_layer = base_model.get_layer(last_conv_layer_name)
    last_conv_model = keras.Model(base_model.input, last_conv_layer.output)

    with tf.GradientTape() as tape:
        x = data_augmentation(img_array, training=False)
        x = keras.applications.resnet50.preprocess_input(x)
        conv_outputs = last_conv_model(x)
        preds = classifier_model(conv_outputs, training=False)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads[0], axis=(0, 1))
    conv_outputs = conv_outputs[0]
    heatmap = tf.reduce_sum(pooled_grads * conv_outputs, axis=-1)
    heatmap = tf.nn.relu(heatmap)
    heatmap /= tf.reduce_max(heatmap) + 1e-8
    return heatmap.numpy()

def resize_heatmap_to_image(heatmap, target_size):
    return tf.image.resize(heatmap[..., np.newaxis], target_size).numpy().squeeze()

def blend_heatmap_with_image(original_image, heatmap_resized, alpha=0.4):
    img = np.clip(original_image, 0, 255).astype("float32")
    colormap = cm.get_cmap("jet")
    heatmap_color = np.uint8(255 * colormap(heatmap_resized)[:, :, :3]).astype("float32")
    blended = img * (1 - alpha) + heatmap_color * alpha
    return np.clip(blended, 0, 255).astype("uint8")
