
ShareShot is a Kivy-based application that simplifies the process of capturing and sharing images using your device's camera. It integrates with Filestack to upload images and generate shareable links effortlessly.

Features
Camera Screen: Capture images using your device's camera.
Image Screen: Upload captured images to Filestack and generate shareable links.
Copy Link: Copy the generated link to the clipboard.
Open Link: Open the generated link in the default web browser.


Installation
Prerequisites
Python 3.6+
Kivy 2.3.0
Filestack Python library

Installation Steps

1.Clone the repository:

git clone https://github.com/akshayjith4/shareshot.git
cd shareshot



2.Install dependencies:

pip install -r requirements.txt



3.Set up Filestack API key:

Obtain a Filestack API key from Filestack.
Create a secret directory in the root of the project.
Inside secret, create a Python file named filestack_apikey.py.
Add your API key to filestack_apikey.py:
API_KEY = 'your_actual_filestack_api_key_here'



4.Run the application:

python main.py


Usage
Start Camera: Opens the camera to capture images.
Capture: Takes a picture and saves it locally.
Create Sharable link: Uploads the captured image to Filestack and displays the generated link.
Copy Link: Copies the generated link to the clipboard.
Open Link: Opens the generated link in the default web browser.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.


Acknowledgments
Built using Kivy
Uses the Filestack Python library
