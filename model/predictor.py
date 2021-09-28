import tensorflow as tf
import numpy as np
from keras.applications import mobilenet_v2
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.layers import GlobalAveragePooling2D, Dropout, Dense
from settings import PATH_TO_MODEL


class StickerPredictor:

    def __init__(self):
        self.class_names = ['no_sticker', 'sticker']

        base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
        base_model.trainable = True
        for layer in base_model.layers[:140]:
            layer.trainable = False

        inputs = tf.keras.Input(shape=(224, 224, 3))
        x = mobilenet_v2.preprocess_input(inputs)
        x = base_model(x, training=False)
        x = GlobalAveragePooling2D()(x)
        x = Dropout(0.2)(x)
        outputs = Dense(1, kernel_regularizer=tf.keras.regularizers.l2(0.01))(x)
        self.model = tf.keras.Model(inputs, outputs)
        self.model.load_weights(PATH_TO_MODEL)

    def prepare_image(self, image, target=(224, 224)):
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize(target)
        image = np.array(image)
        image = np.expand_dims(image, axis=0)

        return image

    def predict(self, image):
        prob = self.model.predict(image)
        prob = tf.nn.sigmoid(prob)
        prediction = 0 if prob < 0.5 else 1
        label = self.class_names[prediction]
        return label, prob
