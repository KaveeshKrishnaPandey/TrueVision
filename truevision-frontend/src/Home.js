/*
 home.js

 This file defines the Home component of the TrueVision application. 
 It provides the main functionality for users to upload an image, 
 process it through the deepfake detection backend, and display the results, 
 including the prediction ("Deepfake" or "Real") and the confidence level.

*/



import React, { useState } from "react";
import axios from "axios";

// Home component for the TrueVision application
function Home() {
  // State variables to manage file input, predictions, and processing status
  const [file, setFile] = useState(null); // Selected file
  const [fileName, setFileName] = useState(""); // File name of the uploaded file
  const [prediction, setPrediction] = useState(null); // Prediction result: "Real" or "Deepfake"
  const [confidence, setConfidence] = useState(null); // Confidence level of the prediction
  const [isProcessing, setIsProcessing] = useState(false); // Indicates if the detection is in progress

  // Handle file selection and update states
  const handleFileUpload = (e) => {
    const selectedFile = e.target.files[0]; // Get the selected file
    if (selectedFile) {
      setFile(selectedFile);
      setFileName(selectedFile.name);
      setPrediction(null);
      setConfidence(null);
    }
  };

  // Handle deepfake detection using the uploaded image
  const handleDetectFake = async () => {
    if (!file) {
      alert("Please upload an image first!"); // Alert if no file is selected
      return;
    }

    // Prepare the file to be sent as FormData
    const formData = new FormData();
    formData.append("file", file);

    try {
      setIsProcessing(true); // Indicate that processing is ongoing
      setPrediction(null);
      setConfidence(null);

      // Send a POST request to the Flask server
      const response = await axios.post("https://truevision.onrender.com/upload", formData);
      const { prediction, confidence } = response.data; // Extract prediction and confidence from the response
      setPrediction(prediction);
      setConfidence(confidence);
    } catch (error) {
      console.error("Error during image processing:", error); // Print any errors
      alert("An error occurred while processing the image. Please make sure that the Backend (main.py) is running."); // Show error alert to the user
    } finally {
      setIsProcessing(false); // Reset processing status
    }
  };

  // Render the UI components
  return (
    <section className="intro">
      <div className="content-wrapper">
        {/* Text section for the introduction */}
        <div className="intro-text">
          <h1>
            <span className="true-text">True</span>
            <span className="vision-text">Vision</span>
          </h1>
          <p>Upload an image for deepfake detection. Supported file formats:</p>
          <p>(.jpg, .jpeg, .png, .webp, .bmp)</p>

          {/* Upload button styled as a label */}
          <label htmlFor="file-upload" className="upload">
            Upload Image
          </label>
          {/* Hidden file input field for image upload */}
          <input
            id="file-upload"
            type="file"
            accept="image/*"
            onChange={handleFileUpload} // Trigger handleFileUpload on file selection
            style={{ display: "none" }} // Hidden input field
          />

          {/* Button to start the deepfake detection */}
          <button className="detect" onClick={handleDetectFake}>
            Detect Fake
          </button>

          {/* Display the selected file name */}
          {fileName && <p className="file-name">Selected File: {fileName}</p>}
          {/* Show processing status */}
          {isProcessing && <p className="processing">Processing...</p>}

          {/* Display prediction results */}
          {prediction && (
            <div className="result">
              
              {prediction === "Deepfake" ? (
                <p className="result-fake">Prediction: ❌ AI Generated</p>
              ) : (
                <p className="result-real">Prediction: ✔ Real</p>
              )}
              {/* Confidence level styled according to the prediction */}
              <p style={{ color: prediction === "Deepfake" ? "#FF0000" : "#00FF00" }}>
                Confidence: {confidence}%
              </p>
            </div>
          )}
        </div>

        
        <div className="intro-image">
          <img
            src={`${process.env.PUBLIC_URL}/TrueVision Logo.png`} // Dynamic public URL for the logo
            alt="App Logo"
          />
        </div>
      </div>
    </section>
  );
}

export default Home;
