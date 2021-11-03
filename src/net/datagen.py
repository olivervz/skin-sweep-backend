import numpy as np
import keras.applications.mobilenet as mobilenet

from keras import backend as K
from keras.layers.core import Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.metrics import top_k_categorical_accuracy
from keras.models import Model
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.optimizers import Adam


def top_2_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=2)


def top_3_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=3)


training_dir = '../../data/ham10000/images/'
validation_dir = '../../data/ham10000/validation'

training_count = 10015
validation_count = 195

training_batch_size = 10
validation_batch_size = 10

image_size = 224  # MobileNet uses 224x224 inputs

num_training_steps = np.ceil(training_count / training_batch_size)
num_validation_steps = np.ceil(validation_count / validation_batch_size)

# Preprocess datasets for MobileNet input
training_batches = ImageDataGenerator(
    preprocessing_function=mobilenet.preprocess_input
).flow_from_directory(
    training_dir,
    target_size=(image_size, image_size),
    batch_size=training_batch_size
)

validation_batches = ImageDataGenerator(
    preprocessing_function=mobilenet.preprocess_input
).flow_from_directory(
    validation_dir,
    target_size=(image_size, image_size),
    batch_size=validation_batch_size
)

testing_batches = ImageDataGenerator(
    preprocessing_function=mobilenet.preprocess_input
).flow_from_directory(
    validation_dir,
    target_size=(image_size, image_size),
    batch_size=validation_batch_size,
    shuffle=False
)

# Generate MobileNet model
net = mobilenet.MobileNet()
x = net.layers[-6].output

# Add dropout layer to avoid overfitting
dropout = Dropout(0.25)(x)

# Add dense layer to give prediction
predictions = Dense(7, activation='softmax')(x)

# Create new model with modified mobilenet
model = Model(inputs=net.input, outputs=predictions)

# Only train on the last 23 layers
for layer in model.layers[:-23]:
    layer.trainable = False

model.compile(
    Adam(lr=0.01),
    loss='categorical_crossentropy',
    metrics=[K.categorical_crossentropy, top_2_accuracy, top_3_accuracy]
)

output_file = 'skinsweep.model'

checkpoint = ModelCheckpoint(
    output_file,
    monitor='val_top_3_accuracy',
    verbose=1,
    save_best_only=True,
    mode='max'
)

reduce_lr = ReduceLROnPlateau(
    monitor='val_top_3_accuracy',
    factor=0.5,
    patience=2,
    berbose=1,
    mode='max',
    min_lr=0.00001
)

callbacks = [checkpoint, reduce_lr]

history = model.fit_generator(
    training_batches,
    steps_per_epoch=num_training_steps,
    validation_data=validation_batches,
    validation_steps=num_validation_steps,
    epochs=10,
    verbose=1,
    callbacks=callbacks
)
