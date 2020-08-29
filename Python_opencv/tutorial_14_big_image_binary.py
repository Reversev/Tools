#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    big image adaptive threshold
"""
import cv2 as cv
import numpy as np


# 将大图片拆分成小图片后再用自适应局部阈值比较好
def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            print(np.std(roi), np.mean(roi))
            # dev = np.std(roi)
            # if dev < 15:
            #     gray[row:row+ch, col:col+cw] = 255
            # else:
            #     ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            #     gray[row:row + ch, col:col + cw] = dst
            # ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row:row+ch, col:col+cw] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("./result_binary.png", gray)


print("--------------Hello Python ------------")
src = cv.imread("./images/big_image.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
big_image_binary(src)
cv.waitKey(0)   # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
