#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    simple blur
    median blur
    custom blur(自定义的中值滤波)
"""
import cv2 as cv
import numpy as np


def blur_demo(image):
    # dst = cv.blur(image, (1, 6))  # 竖直方向(1, 6) 水平方向：(6, 1)
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_demo", dst)


def median_blur(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur", dst)


def custom_blur(image):
    # kernel = np.ones([5, 5], np.float32)/25   # 自定义的中值滤波
    # kernel = np.array([(1, 1, 1), (1, 1, 1), (1, 1, 1)], np.float32) / 9
    kernel = np.array([(0, -1, 0), (-1, 5, -1), (0, -1, 0)], np.float32)  # 锐化算子must odd, tol_value=0/1
    dst = cv.filter2D(image, -1, kernel)
    cv.imshow("custom_blur", dst)


print("--------------Hello Python ------------")
src = cv.imread("./images/example.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
median_blur(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
