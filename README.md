**NOTE:** The training dataset did not include cartoon style human AI-images, it was trained to detect Deepfakes which are created by *Morphing Human Faces*. This limitation occurred due to the huge time taken by Model Training and can also cause some wrong predections.


# Purpose of the different files and folders:

1. **main.py** --> This is the main app which processes the images (Backend)

2. **train_model.py** --> This python file is used to train the Deepfake Detection Model (truevision_model.h5)

3. **truevision_model.h5** --> This is the actual trained Deepfake Detection Model.

4. **requirements.txt** --> This text file contains all the Dependencies required to run *main.py* and *train_model.py*

5. **uploads** --> This folder is where the user given images are stored.

6. **data** --> This folder stores images for training the model.

7. **Testing-Images** --> This folder contains a few images which you can use to test the working of this app. The images in this folder have not been used to train the model.

8. **truevision-frontend** --> In this folder, all the code files for the *Frontend* is present.


# --------------------------------------------------
# --------------------------------------------------


# Setup and installation instructions:

**Important Versions (Please make sure to use the versions mentioned below to avoid errors)**
1. **Python** --> 3.10.0
2. **Node.js** --> 22.12.0


**Setting up the Backend**
1. Open a terminal *(Command Prompt/Git Bash)* in the main directory **(TrueVision)**

2. Create Virtual Environment (Make sure to use Python 3.10.0)
   --> [python -m venv truevision_venv] 

3. Activate the Virtual Environment
   --> [source truevision_venv/Scripts/activate] (For Git Bash)

   --> [truevision_venv\Scripts\activate] (For cmd)

4. Install the Dependencies for Backend
   --> [pip install -r requirements.txt]


**Setting up the Frontend**
1. Open a new terminal *(Command Prompt/Git Bash)* in the frontend directory **(TrueVision/truevision-frontend)**

2. Install the Dependencies for the Frontend react app
   --> [npm install]

**You may keep these two terminals open to run the app**


# --------------------------------------------------
# --------------------------------------------------


# Instructions for running the app
1. In the terminal you used to setup the backend, run the *main.py* file
   --> [python app.py]
   (The backend server will start on localhost:5000)

**When you see the following kind of message on the terminal, that means the backend is live:**
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx

2. In the terminal you used to setup the frontend, run the react app
   --> [npm start]
   (The app will start on localhost:3000)

**When you see the following kind of message on the terminal, that means the frontend is live:**
 * webpack compiled successfully


# --------------------------------------------------
# --------------------------------------------------


# The model is already trained, but in order to run the *train_model.py* here are the steps:
1. Paste all the images *real and fake* in the *validation and training* folders inside the *data* folder present in the main directory.

2. Open a terminal in the main directory *(TrueVision)*

3. Activate the Virtual Environment (Set the venv first if not already)
   --> [source truevision_venv/Scripts/activate] (For Git Bash)

   --> [truevision_venv\Scripts\activate] (For cmd)

4. Run the file (Install all the Dependencies from the *requirement.txt* if not already)
   --> [python train_model.py]


# --------------------------------------------------
# --------------------------------------------------


# Necessary Python Libraries (Python --> 3.10.0):
1. Flask==2.3.2
2. flask_cors==5.0.0
3. tensorflow==2.11.0
4. numpy==1.23.5
5. opencv-python==4.7.0.72
6. Werkzeug==3.1.3
7. Pillow==11.0.0
8. scipy==1.10.1


# Developer --> Kaveesh Krishna Pandey
**Thank You For Having A Look At My Project :)**