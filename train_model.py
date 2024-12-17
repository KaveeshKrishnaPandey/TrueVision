"""
train_model.py

This script defines and trains a deepfake detection model for binary classification (real or fake). 
It uses a Convolutional Neural Network (CNN) to learn features from images and predict their authenticity. 
The model is trained on data organized in separate directories for 'real' and 'fake' images. 
Once training is complete, the model is saved for later use, and the system is shut down for efficiency.

Key Features:
1. Loads and preprocesses images dynamically from directories.
2. Implements a CNN for binary image classification.
3. Saves the trained model to disk after training.
4. Includes automatic system shutdown upon completion.
"""

# Necessary Imports
import os  # For file and system operations
import time  # To delay system shutdown
import numpy as np  # For numerical operations
import cv2  # For image manipulation
import scipy.ndimage  # For additional image processing if needed
from tensorflow.keras.models import Sequential  # For building the CNN model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # CNN layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # For image augmentation
from tensorflow.keras.optimizers import Adam  # Optimizer for training

# Define the CNN model structure
def create_model():
    """
    This function creates and compiles a Convolutional Neural Network (CNN) model 
    designed for binary classification (deepfake detection).

    Returns:
        model (Sequential): A compiled Keras Sequential model.
    """
    model = Sequential()
    # Add a convolutional layer with 32 filters and a 3x3 kernel, followed by ReLU activation
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
    # Add a max pooling layer to reduce spatial dimensions
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Add a second convolutional layer with 64 filters
    model.add(Conv2D(64, (3, 3), activation='relu'))
    # Add another max pooling layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Flatten the 2D feature maps into a 1D vector
    model.add(Flatten())
    # Add a fully connected layer with 128 neurons and ReLU activation
    model.add(Dense(128, activation='relu'))
    # Add dropout to prevent overfitting
    model.add(Dropout(0.5))
    # Add the output layer with a sigmoid activation function for binary classification
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model using Adam optimizer and binary cross-entropy loss
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Train the CNN model
def train_model():
    """
    This function handles the training of the CNN model. 
    It preprocesses training and validation data, fits the model, saves it, and initiates a system shutdown.
    """
    # Configure data augmentation for the training set
    train_datagen = ImageDataGenerator(
        rescale=1./255,  # Normalize pixel values to [0, 1]
        shear_range=0.2,  # Apply random shearing
        zoom_range=0.2,  # Apply random zoom
        horizontal_flip=True  # Allow random horizontal flipping
    )

    # Configure data augmentation for the validation set (only rescaling)
    test_datagen = ImageDataGenerator(rescale=1./255)

    # Create a data generator for the training set
    train_generator = train_datagen.flow_from_directory(
        './data/train',  # Directory containing 'real' and 'fake' subdirectories for training
        target_size=(150, 150),  # Resize all images to 150x150
        batch_size=32,  # Number of images per batch
        class_mode='binary'  # Binary classification labels (0 or 1)
    )

    # Create a data generator for the validation set
    validation_generator = test_datagen.flow_from_directory(
        './data/validation',  # Directory containing validation data
        target_size=(150, 150),  # Resize images to 150x150
        batch_size=32,  # Number of images per batch
        class_mode='binary'  # Binary classification labels (0 or 1)
    )

    # Build the CNN model
    model = create_model()

    # Train the model using the training data generator
    model.fit(
        train_generator,  # Training data
        epochs=1,  # Number of training epochs
        validation_data=validation_generator  # Validation data for evaluation
    )

    # Save the trained model to disk
    model.save('truevision_model.h5')
    print("Training complete. Shutting down the system...")

    # Wait 10 seconds before shutting down the system
    time.sleep(10)

    # Shutdown the system (Windows-specific command)
    os.system("shutdown /s /t 1")

# Main entry point
if __name__ == "__main__":
    train_model()
