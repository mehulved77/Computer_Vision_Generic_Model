from keras.datasets import mnist
from keras.utils import to_categorical
import numpy as np
from pprint import pprint

from keras import backend as K
K.set_image_dim_ordering('tf')

seed = 7
np.random.seed(seed)

# Set up dataset specific values
batch_size = 128
num_classes = 10

# input image dimensions
img_rows, img_cols = 28, 28

# Load dataset
# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# (for MLP only) flatten 28*28 images to a 784 vector for each image
#num_pixels = x_train.shape[1] * x_train.shape[2]
#X_train = x_train.reshape(x_train.shape[0], num_pixels).astype('float32')
#X_test = x_test.reshape(x_test.shape[0], num_pixels).astype('float32')

# (for CNNs)
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# reshape to be [samples][width][height][channels]
# x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
# x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32')

# normalize inputs from 0-255 to 0-1
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
pprint(y_train)
pprint(y_test)
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
