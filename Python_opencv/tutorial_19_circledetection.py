#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

import cv2 as cv
import numpy as np


# Hough Circle 在xy坐标系中一点对应Hough坐标系中的一个圆，xy坐标系中圆上各个点对应Hough坐标系各个圆，
# 相加的一点，即对应xy坐标系中圆心
# 现实考量：Hough圆对噪声比较敏感，所以做hough圆之前要中值滤波，
# 基于效率考虑，OpenCV中实现的霍夫变换圆检测是基于图像梯度的实现
def detect_hough_circles(image):
    dst = cv.pyrMeanShiftFiltering(image, 18, 90)    # EPF边缘保留滤波
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 30, param1=50, param2=30)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("detect_hough_circles", image)


print("--------------Hello Python ------------")
src = cv.imread("./images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
detect_hough_circles(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
