#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

"""
    Video of computer(PC)
    Get image info
"""
import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("./images/result.png", src)
cv.waitKey(0)   # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口
cv.destroyAllWindows()

# video_demo()
