#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    plot simple image histogram
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("histogram")


def image_hist(image):
    # h, w, c = image.shape
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
image_hist(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
