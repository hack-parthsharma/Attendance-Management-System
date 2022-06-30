DEBUG_FLAG = 1

# library imports
import os
import cv2
import csv
import numpy as np
from PIL import ImageTk, Image
from student import student

# haarcascade path
haarcascade_path = 'ml_helpers/haarcascade_frontalface_default.xml'
# training image label path
trainimagelabel_path = 'ml_helpers/Trainner.yml'
# train image path
trainimage_path = 'TrainingImages/'
# attendance path
attendance_path = 'Attendance/'

class register:
    target_student = student('','')

    def new_student(self, name, registration_number):
        self.target_student.name = name
        self.target_student.registration_number = registration_number
        if DEBUG_FLAG:
            print("🚩 "+self.target_student.name)
            print("🚩 "+ self.target_student.registration_number)
        register.take_images(self)

    def write_to_register(self, registraion_number, name):
        row = [registraion_number, name]
        try:
            with open(
                "StudentDetails/studentdetails.csv",
                "a+",
            ) as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for ER No:" + registraion_number + " name:" + name
        except FileExistsError as F:
            F = "Student Data already exists"


    def take_images(self):
        try:
            if DEBUG_FLAG:
                print("🚩 In try")
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcascade_path)
            name = self.target_student.name
            registraion_number = self.target_student.registration_number
            image_number = 0
            dir = registraion_number+"-"+name
            path = os.path.join(trainimage_path, dir)
            os.mkdir(path)
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    image_number = image_number + 1
                    cv2.imwrite(
                        f"{path}/ "
                        + name
                        + "_"
                        + registraion_number
                        + "_"
                        + str(image_number)
                        + ".jpg",
                        gray[y : y + h, x : x + w],
                    )
                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif image_number >= 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            self.write_to_register(self,registraion_number, name)
        except FileExistsError as F:
            F = "Student data already exists"
    if DEBUG_FLAG:
        print("🚩 Done with try")
        
