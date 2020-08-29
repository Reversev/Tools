#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

import cv2 as cv
import numpy as np


# 关于霍夫变换的相关知识 https://blog.csdn.net/kbccs/article/details/79641887
def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)

    lines = cv.HoughLines(edges, 3, np.pi/180, 200)
    # cv2.HoughLines()返回值就是（ρ,θ）。ρ 的单位是像素，θ 的单位是弧度。
    # 这个函数的第一个参数是一个二值化图像，所以在进行霍夫变换之前要首先进行二值化，或者进行 Canny 边缘检测。
    # 第二和第三个值分别代表 ρ 和 θ 的精确度。第四个参数是阈值，只有累加其中的值高于阈值时才被认为是一条直线，
    # 也可以把它看成能 检测到的直线的最短长度（以像素点为单位）。
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*a)
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*a)
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("image-lines", image)


def line_detect_possible(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 3, np.pi/180, 100, minLineLength=50, maxLineGap=20)
    for line in lines:
        print(line)
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detect_possible", image)


print("--------------Hello Python ------------")
src = cv.imread("./images/18_line.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
line_detect_possible(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
