#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    Gaussian bilateral blur(MeanShift): pyrMeanShiftFiltering
    Gaussian bilateral blur: bilateralFilter
"""
import cv2 as cv
import numpy as np


# Gaussian bilateral blur
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


# Gaussian bilateral blur
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# shift_demo(src)   # maybe over blur.
bi_demo(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
