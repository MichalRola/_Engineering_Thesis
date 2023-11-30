import numpy as np
import os
import sklearn.utils
import sklearn.preprocessing
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import keras
from keras import layers


# Ścieżka zawierająca obrazy zbiory danych
load_path = r"D:\Folders\_Engineering_Thesis\Data\Datasets"

features = np.load(os.path.join(load_path,'features_training_HTK.npy'))
labels = np.load(os.path.join(load_path,'labels_training_HTK.npy'))

coding = sklearn.preprocessing.LabelEncoder()
coding.fit(labels)

labels_coded = coding.transform(labels)

features = np.swapaxes(features, 1, -1)
features = np.swapaxes(features, 1, 2)

X_train, y_train = sklearn.utils.shuffle(features, labels_coded)

# Definiowanie modelu
num_classes = 10
input_shape = (128, 87, 1)
batch_size = 100
epochs = 30 # epoki uczenia modelu, jedna epoka to przedstawienie wszystkich przykładów modelowi

model = keras.Sequential(
        [
            keras.Input(shape=input_shape),
            keras.layers.Flatten(),
            layers.Dense(num_classes, activation="softmax")
        ]
    )

model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# Koniec definicji modelu

model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)