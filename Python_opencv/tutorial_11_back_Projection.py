#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    inverse project
    histogram 2D
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# OpenCV 提供的函数 cv2.calcBackProject() 可以用来做直方图反向投影。
# 它的参数与函数 cv2.calcHist 的参数基本相同。其中的一个参数是我 们要查找目标的直方图。
# 同样再使用目标的直方图做反向投影之前我们应该先对其做归一化处理。
# 返回的结果是一个概率图像
def back_projection():
    """
    反向投影可以用来做图像分割，或者在图像中找寻我们感兴趣的部分。
    它会输出与输入图像（待搜索）同样大小的图像，其中的每一个像素值代表了输入图像上对应点属于目标对象的概率。
    输出图像中像素值越高（越白）的点就越可能代表我们要搜索的目标 （在输入图像所在的位置）。
    直方图投影经常与camshift 算法等一起使用。
    步骤：
    1. 为一张包含我们要查找目标的图像创建直方图，我们要查找的对象要尽量占满这张图像。
       最好使用颜色直方图，因为一个物体的颜色要比它的灰度能更好的被用来进行图像分割与对象识别。
    2. 再把这个颜色直方图投影到输入图像中寻找我们的目标，
       也就是找到输入图像中的每一个像素点的像素值在直方图中对应的概率，这样我们就得到一个概率图像。
    3. 设置适当的阈值对概率图像进行二值化
    """
    sample = cv.imread("./images/11_2.jpg")
    target = cv.imread("./images/11_1.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
    # cv.NORM_MINMAX对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
    # 归一化后的图像便于显示，归一化后到0,255之间了
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)


def hist2d(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [32, 32], [0, 180, 0, 256]) # [32, 32] can be samller or divide randomly
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
back_projection()
cv.waitKey(0)   # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
