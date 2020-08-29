#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

import cv2 as cv
import numpy as np


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshold value: %s " % ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    outImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        erea = cv.contourArea(contour)  # 计算轮廓的面积

        # 轮廓周长,第二参数可以用来指定对象的形状是闭合的（True）,还是打开的（一条曲线）。
        perimeter = cv.arcLength(contour, True)
        print("contour perimeter:", perimeter)

        x, y, w, h = cv.boundingRect(contour)  # 用矩形画出轮廓
        rate = min(w, h) / max(w, h)
        print("rectangle rate: %s" % rate)
        mm = cv.moments(contour)
        # print("moment:", type(mm))   # moment: <class 'dict'>

        # 计算对象的重心
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']

        cv.circle(dst, (np.int(cx), np.int(cy)), 2, (0, 255, 255), -1)
        cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour erea: %s" % erea)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        """cv.approxPolyDP(contour, epsilon, True) 参数解释
            .   @param curve Input vector of a 2D point stored in std::vector or Mat
            .   @param approxCurve Result of the approximation. The type should match the type of the input curve.
            .   @param epsilon Parameter specifying the approximation accuracy. This is the maximum distance
            .   between the original curve and its approximation.
            .   @param closed If true, the approximated curve is closed (its first and last vertices are
            .   connected). Otherwise, it is not closed.
        """
        # 将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定。
        # 为了帮助理解，假设从一幅图像中查找一个矩形，但是由于图像的种种原因，我们不能得到一个完美的矩形，
        # 而是一个“坏形状”（如下图所示）。
        # 现在你就可以使用这个函数来近似这个形状（）了。
        # 这个函数的第二个参数叫 epsilon，它是从原始轮廓到近似轮廓的最大距离。
        # 它是一个准确度参数。选择一个好的 epsilon 对于得到满意结果非常重要。

        print(approxCurve.shape)
        if approxCurve.shape[0] > 6:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
    cv.imshow("measure_object", dst)


print("--------------Hello Python ------------")
src = cv.imread("./images/handwriting.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
measure_object(src)
cv.waitKey(0)   # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()

