import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Set paths for the dataset
train_data_dir = 'F:/diabetic-retinopathy-detection/train'
test_data_dir = 'F:/diabetic-retinopathy-detection/test'



