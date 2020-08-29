#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    source: github:opencv/sources/sample/data
    (1) add, subtract, divide, multiply, logic-deal(not, and, or)
    (2) contras brightness
    (3) others: mean, std, meanStdDev.
"""

import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def logic_demo(m1, m2):
    # dst = cv.bitwise_and(m1, m2)
    dst = cv.bitwise_or(m1, m2)
    # cv.imshow("logic_and_demo", dst)
    cv.imshow("logic_or_demo", dst)

    # image = cv.imread("./demo.png")
    # cv.imshow("input_demo", image)
    # dst = cv.bitwise_not(image)
    # cv.imshow("logic_not_demo", dst)


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)


def others(m1, m2):
    M1 = cv.mean(m1)
    M2 = cv.mean(m2)
    dev1 = cv.meanStdDev(m1)
    dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


if __name__ == '__main__':
    print("--------------Hello Python ------------")
    src1 = cv.imread("./images/up.jpg")
    src2 = cv.imread("./images/right.jpg")
    print(src1.shape)
    print(src2.shape)
    cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
    cv.imshow("image1", src1)
    cv.imshow("image2", src2)
    src = cv.imread("./images/demo.jpg")
    cv.imshow("image3", src)
    contrast_brightness_demo(src, 1.2, 10)   # 1.2:对比度；10：亮度
    cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

    cv.destroyAllWindows()
