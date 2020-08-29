#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    equalize Histogram: 全局直方图均衡化，用于增强图像对比度，即黑的更黑，白的更白
    clahe: 局部直方图均衡化
    create_rgb_hist: 创建直方图
    hist_compare： 直方图比较：卡方， 巴氏距离，相关性。
"""
import cv2 as cv
import numpy as np


def equal_Hist(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equal_demo", dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    # IMG = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cv.imshow("clahe_demo", dst)


# 创建直方图
def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)  # must float32
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image([row, col, 0])
            g = image([row, col, 1])
            r = image([row, col, 2])
            index = (b/bsize)*16*16 + (g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


# 利用直方图比较相似性，用巴氏和相关性比较好
def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离： %s, 相关性： %s, 卡方： %s" % (match1, match2, match3))


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
clahe_demo(src)
image1 = cv.imread("./images/rice.png")
image2 = cv.imread("./images/noise_rice.png")
# hist_compare(image1, image2)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
