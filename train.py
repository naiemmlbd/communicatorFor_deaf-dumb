from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.optimizers import RMSprop, Adam
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Flatten, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K

from keras.utils.vis_utils import plot_model
from matplotlib import pyplot as plt
from time import time

img_rows, img_cols = 128, 128

VGG = VGG16(weights='imagenet', include_top=False,
            input_shape=(img_rows, img_cols, 3))

for layer in VGG.layers:
    layer.trainable = False


def addTopModelVGG(bottom_model, num_classes):

    top_model = bottom_model.output
    top_model = GlobalAveragePooling2D()(top_model)
    top_model = Dense(512, activation='relu')(top_model)
    top_model = Dense(256, activation='relu')(top_model)
    top_model = Dense(256, activation='relu')(top_model)
    top_model = Dense(128, activation='relu')(top_model)
    top_model = Dense(128, activation='relu')(top_model)
    top_model = Dense(num_classes, activation='softmax')(top_model)

    return top_model


num_classes = 26

FC_Head = addTopModelVGG(VGG, num_classes)

model = Model(inputs=VGG.input, outputs=FC_Head)

print(model.summary())

train_data_dir = '/Users/jhasan/3rd_attempt/train'
validation_data_dir = '/Users/jhasan/3rd_attempt/test'

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.3,
    height_shift_range=0.3,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1./255)

batch_size = 32

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical')


checkpoint = ModelCheckpoint(
    'trained_model.h5',
    monitor='val_loss',
    mode='min',
    save_best_only=True,
    verbose=1)

earlystop = EarlyStopping(
    monitor='val_loss',
    min_delta=0,
    restore_best_weights=True,
    patience=10,
    verbose=1)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_loss',
                                            patience=5,
                                            verbose=1,
                                            factor=0.2,
                                            min_lr=0.0001)

callbacks = [earlystop, checkpoint, learning_rate_reduction]

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001),
              metrics=['accuracy']
              )

nb_train_samples = 5200
nb_validation_samples = 1300

epochs = 50
batch_size = 32

history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples//batch_size,
    epochs=epochs,
    callbacks=callbacks,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples//batch_size)

print(history.history.keys())
plot_model(model, to_file='model.png')

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
