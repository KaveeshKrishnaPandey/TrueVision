"""
main.py

This is the backend server for the TrueVision application. It handles file uploads, processes images using a trained deepfake detection model (truevision_model.h5), and returns predictions along with confidence scores. The server is built using Flask and integrates with a TensorFlow/Keras model to provide AI-based analysis.
"""

# Necessary Imports
from flask import Flask, request, jsonify  # Import Flask for API creation and utilities
from flask_cors import CORS  # Enable Cross-Origin Resource Sharing (CORS)
from werkzeug.utils import secure_filename  # Safely handle uploaded file names
import os  # OS module for file path operations
import numpy as np  # Numerical operations library
import cv2  # OpenCV for image processing
from tensorflow.keras.models import load_model  # To load the trained Keras model
from tensorflow.keras.preprocessing.image import img_to_array  # To preprocess images into arrays

# Initialize Flask app
app = Flask(__name__)  # Create an instance of the Flask application

# Enable CORS for all routes
CORS(app)  # Allow requests from different origins, useful for frontend-backend interaction
app.config['UPLOAD_FOLDER'] = './uploads'  # Define the folder to store uploaded files

# Load the trained model
model = load_model('truevision_model.h5')  # Load the pre-trained Keras model for deepfake detection

@app.route('/upload', methods=['POST'])  # Define an API endpoint for file uploads

def upload_file():
    try:
        # Retrieve the uploaded file
        file = request.files['file']  # Access the uploaded file from the request
        filename = secure_filename(file.filename)  # Ensure the filename is safe to use
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Build a secure file path
        file.save(file_path)  # Save the uploaded file to the server

        # Pre-process the image for model prediction
        img = cv2.imread(file_path)  # Read the image from the saved file
        img = cv2.resize(img, (150, 150))  # Resize the image to match the model's input size
        img = img_to_array(img) / 255.0  # Convert the image to a NumPy array and normalize pixel values
        img = np.expand_dims(img, axis=0)  # Add a batch dimension to match the model's input shape

        # Perform prediction using the model
        prediction = model.predict(img)  # Predict whether the image is a deepfake or real
        print(f"Prediction probabilities: {prediction}, {prediction[0][0]}")  # Print the raw probabilities for debugging

        # Process prediction to generate a label and confidence score
        prediction_label = "Deepfake" if prediction[0][0] < 0.45 else "Real"  # Determine the prediction label
        confidence = (prediction[0][0] * 100) if prediction_label == "Real" else ((1 - prediction[0][0]) * 100)  # Calculate confidence

        # Send the response back to the client
        return jsonify({'prediction': prediction_label, 'confidence': round(confidence, 2)})  # Return prediction and confidence

    except Exception as e:
        # Handle errors and return an error response
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({'error': str(e)}), 500  # Send an error message to the client

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode, enabling live reloading and error messages
