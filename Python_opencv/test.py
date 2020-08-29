#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    The code uses to display demo(picture).
"""
import cv2 as cv


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
