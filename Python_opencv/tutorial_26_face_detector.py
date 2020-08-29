#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

import cv2 as cv
import numpy as np


def face_detect(image, source_path):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(source_path)
    faces = face_detector.detectMultiScale(gray, 1.02, 26)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv.imshow("face_detection", image)


print("--------------Hello Python ------------")
src = cv.imread("./images/faces.jpg")
# 视频检测
# capture = cv.VideoCapture(0)
# while True:
#     ret, frame = capture.read()
#     frame = cv.flip(frame, 1)
#     face_detect(frame)
#     c = cv.waitKey(10)
#     if c == 27:   # Esc:stop
#         break

cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# source_path = "D:\\Python_opencv\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml"
source_path = "D:\\Python_opencv\\data\\lbpcascades\\lbpcascade_frontalface.xml"
face_detect(src, source_path)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
