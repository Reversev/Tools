#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    分水岭算法原理：
      任何一副灰度图像都可以被看成拓扑平面，灰度值高的区域可以被看成是 山峰，灰度值低的区域可以被看成是山谷。
    我们向每一个山谷中灌不同颜色的水。随着水的位的升高，不同山谷的水就会相遇汇合，为了防止不同山谷的水汇合，
    我们需要在水汇合的地方构建起堤坝。不停的灌水，不停的构建堤坝知 道所有的山峰都被水淹没。
    我们构建好的堤坝就是对图像的分割。这就是分水岭算法的背后哲理
      但是这种方法通常都会得到过度分割的结果，这是由噪声或者图像中其他不规律的因素造成的。
    为了减少这种影响，OpenCV 采用了基于掩模的分水岭算法，在这种算法中我们要设置那些山谷点会汇合，那些不会。
    这是一种交互式的图像分割。我们要做的就是给我们已知的对象打上不同的标签。
    如果某个区域肯定是前景或对象，就使用某个颜色（或灰度值）标签标记它。
    如果某个区域肯定不是对象而是背景就使用另外一个颜色标签标记。而剩下的不能确定是前景还是背景的区域就用 0 标记。
    这就是我们的标签。然后实施分水岭算法。
    每一次灌水，我们的标签就会被更新，当两个不同颜色的标签相遇时就构建堤坝，直到将所有山峰淹没，
    最后我们得到的边界对象（堤坝）的值为 -1。
    基于距离的分水岭分割流程：
    输入图像->灰度->二值->距离变换->寻找种子->生成marker->分水岭变换->输出图像
"""
import cv2 as cv
import numpy as np


def watershed(image):
    # remove noise if any
    print(image.shape)
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)
    # gray/binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary-image", binary)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("morphology operation", sure_bg)

    # distance transform
    # Finding sure foreground area
    # 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，
    # 也就是到零像素点的最短距离
    # 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全腐蚀。
    # 这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心像素点的距离。
    # 根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
    # cv2.distanceTransform(src, distanceType, maskSize)
    # 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_
    dist = cv.distanceTransform(mb, cv.DIST_L2, maskSize=3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance-t", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(image, markers=markers)
    image[markers == -1] = [0, 0, 255]
    cv.imshow("result", image)


print("--------------Hello Python ------------")
src = cv.imread("./images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
watershed(src)
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
