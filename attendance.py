# library imports
import os
import cv2
import csv
import numpy as np
from PIL import ImageTk, Image

from register import register

# haarcascade path
haarcascade_path = 'ml_helpers/haarcascade_frontalface_default.xml'
# training image label path
trainimagelabel_path = 'ml_helpers/Trainner.yml'
# train image path
trainimage_path = 'TrainingImages/'
# attendance path
attendance_path = 'Attendance/'



class attendance:
    print("What do you want to do?")
    print("1. Register new student.")
    print("2. Mark attendance")
    choice_str = input()
    choice = int(choice_str)
    
    if choice == 1:
        print("Regestering new student now!")
        name = input("Enter the student's name: ")
        registraion_number = input("Enter the student's registration number: ")
        print(name, registraion_number)
        register.new_student(register, name, registraion_number)
    