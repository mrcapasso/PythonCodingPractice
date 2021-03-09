#Goal: Create a YouTube archive for analysis. 

import pytube #YouTube Downloading Module
    #Documentation: https://pypi.org/project/pytube/

import cv2 #General Video Manipulation Module
    #Documentation: https://docs.opencv.org/master/modules.html

import face_detection, face_recognition
    #Documentation: https://pypi.org/project/face-recognition/
    #face_detection: Isolates face & pixel coordinates
    #face_recognition: Crossreferences faces with unknown and known folder. 
        #Supports multiprocessing & GPU CUDA accel. See docs.
    #Examples: https://github.com/ageitgey/face_recognition/blob/master/README.md#python-code-examples

import shutil, zipfile #General file manipulation and compression
    #Documentation: https://automatetheboringstuff.com/chapter9/

import thread, time #Multithreading module
    #Documentation: https://www.tutorialspoint.com/python/python_multithreading.htm

#* Consider breaking apart script so others can access CSV info w/o video archive

###############################(YT Archive Table)###############################
#YT URL Index
#Title
#Retrival Date
#Upload Date
#Channel Name
#Channel Subscribers
#Total Views
#Like & Dislike Numbers
#Resolution/Quality Options
#Video Length
#Video Description
#Num Distinct Faces

############################(High Density Video Finder)#########################
#Function to find ideal video based off keywords and views.


############################(YT Vid Download and Parse)#########################
#! Multithread this.
#Download YT Video Based on URL & Optimal Resolution
#Identify DISTINCT faces in video (code w/ OpenCV and face_recoginition)
    #Frame Parse Ex: https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_video_file.py
    #Note, need more general and robust solution than example
#Update YT Archive CSV
#Mega-Compress Original Video
