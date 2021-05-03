
<h1 align="center">Face Detection with OpenCV 🎥 </h1>

## Motivation:
This repository was created to contain the face detection Python program using OpenCV.

## Problem Statement:
There are lot of convoluted ways and lengthy code options available out there to solve the problem of face detection, but the Python file uploaded in this repository is a very simple Machine Learning approach. Face detection is the first step for doing face recognition.

## Instructions:
Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. We are using face classifier in this project. You can experiment with other classifiers as well. 

- You need to download the trained classifier XML file (haarcascade_frontalface_default.xml), which is available in OpenCv’s GitHub repository.
- The detection works only on grayscale images/frames from video. So it is important to convert the color image to grayscale.
- detectMultiScale function is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours. 
- scaleFactor specifies how much the image/frame size is reduced with each scale. minNeighbours specifies how many neighbors each candidate rectangle should have to retain it. 
- You may have to tweak these values to get the best results.
- Faces contains a list of coordinates for the rectangular regions where faces were found. We use these coordinates to draw the rectangles over the detected face.

## Library used:
- <a href="https://opencv.org/">OpenCV</a>

## Credits:
- <a href="https://www.youtube.com/">YouTube</a> for tutorials
