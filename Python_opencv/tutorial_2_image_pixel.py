#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    (1) pixels access reversed
    (2) inverse pixels faster
    (3) create image.
    (4) count time.
"""
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s, channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image):
    """"
    opencv实现像素反转faster
    """
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def create_image():
    """
    # mutiply channels
    img = np.zeros([400, 400, 3], dtype=np.uint8)
    # img = np.zeros([400, 400, 3], dtype=np.uint8)    # single channel
    img[:, :, 1] = np.ones([400, 400])*255    # green
    cv.imshow("new image", img)
    """
    m1 = np.ones([3, 3], np.float32)
    m1.fill(122.388)
    print(m1)

    m2 = m1.reshape([1, 9])
    print(m2)

    m3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
    m3.fill(9)
    print(m3)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")  # src: blue green red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time : %s s " % time*1000)
cv.waitKey(0)   # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
