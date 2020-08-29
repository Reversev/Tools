#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

import cv2 as cv
import numpy as np


# 图像梯度（由x,y方向上的偏导数和偏移构成），有一阶导数（sobel算子）和二阶导数（Laplace算子）
# 用于求解图像边缘，一阶的极大值，二阶的零点
# 一阶偏导在图像中为一阶差分，再变成算子（即权值）与图像像素值乘积相加，二阶同理
def Laplacian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)                     # == np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    # kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("Laplacian_demo", lpls)


def sobel_demo(image):
    # grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    # grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient-xy", gradxy)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
Laplacian_demo(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
