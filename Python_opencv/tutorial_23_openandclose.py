#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    开运算:先进性腐蚀再进行膨胀就叫做开运算,它被用来去除噪声。
    闭运算:先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
    这里我们用到的函数是 cv2.morphologyEx()。
    开闭操作作用：
    1. 去除小的干扰块-开操作
    2. 填充闭合区间-闭操作
    3. 水平或垂直线提取,调整kernel的row，col值差异。
    比如：采用开操作，kernel为(1, 15),提取垂直线，kernel为(15, 1),提取水平线，
"""
import cv2 as cv
import numpy as np


def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))    # tiqu shuiping(15, 1)
    # 函数cv2.getStructuringElement() 只需要告诉他你需要的核的形状和大小
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", binary)


def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close-result", binary)


print("--------------Hello Python ------------")
src = cv.imread("./images/23_line2.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
open_demo(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
