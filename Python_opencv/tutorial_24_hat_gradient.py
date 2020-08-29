#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    其他形态学操作：
    顶帽：原图像与开操作之间的差值图像
    黑帽：比操作与原图像直接的差值图像
    形态学梯度：其实就是一幅图像膨胀与腐蚀的差别。 结果看上去就像前景物体的轮廓
    基本梯度：膨胀后图像减去腐蚀后图像得到的差值图像。
    内部梯度：用原图减去腐蚀图像得到的差值图像。
    外部梯度：膨胀后图像减去原图像得到的差值图像。
"""
import cv2 as cv
import numpy as np


def hat_gray(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    # promote lighth
    # cimage = np.array(gray.shape, np.uint8)
    # print(cimage)
    cimage = 120
    dst = cv.add(dst, cimage)
    cv.imshow("top_hat", dst)


def hat_binary(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("top_hat", dst)


def gradient_gb(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    # dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
    cv.imshow("gradient_gb", dst)


def gradient_ie(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # internal gradient
    dst2 = cv.subtract(dm, image)  # external gradient
    cv.imshow("internal gradient", dst1)
    cv.imshow("external gradient", dst2)


print("--------------Hello Python ------------")
src = cv.imread("./images/lena.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
gradient_ie(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
