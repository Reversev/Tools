#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    clamp(normalize)
    add gaussian noise for picture.
"""
import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


# add gaussian noise
def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image", image)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print("time consume: %s s" % time)

# dst = cv.GaussianBlur(src, (0, 0), 15)
dst = cv.GaussianBlur(src, (5, 5), 0)   # gaussian noise : (5, 5)

cv.imshow("Gsussian Blur", dst)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
