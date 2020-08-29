#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    The first function use to read a video file for tracking simple-color picture,
    and display gray and mask picture.
    （1）color_space：gray，hsv，yuv，Ycrcb，HIS.
    (2) count time.
"""
import cv2 as cv
import numpy as np


def extrace_object():
    """
        这个函数用于读取视频文件进行简单的颜色追踪，并显示出黑白mask图片进行展示
    """
    capture = cv.VideoCapture('./demo.mp4')
    while True:
        ret, frame = capture.read()
        if not ret == True:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])  # 绿色的hsv对应的最低值
        high_hsv = np.array([77, 255, 255])  # 绿色的hsv对应的最高值
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
        # dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        # cv.imshow("mask1", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb", Ycrcb)
    his = cv.cvtColor(image, cv.COLOR_BGR2HLS)
    cv.imshow("HIS", his)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")  # src: blue green red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
# channel split
b, g, r = cv.split(src)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
# set channel value. eg: channel 3 set as 0.
src[:, :, 2] = 0
# channel merge
src = cv.merge([b, g, r])
cv.imshow("change image", src)
# extrace_object()
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print("time : %s s " % time * 1000)
cv.waitKey(0)
