#!/usr/bin/env python

import cv2
import sys


def main(argv):

    image = cv2.imread(argv[0])
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh_img = cv2.threshold(gray_image, 100, 255,
                                            cv2.THRESH_BINARY)

    bgr = cv2.cvtColor(thresh_img, cv2.COLOR_GRAY2BGR)
    bgra = cv2.cvtColor(bgr, cv2.COLOR_BGR2BGRA)

    height, width, channels = bgra.shape

    for i in range(height):
        for j in range(width):

            if bgra[i][j][0] == 255:
                bgra[i][j][3] = 0

    cv2.imwrite(argv[1], bgra)


if __name__ == "__main__":
    main(sys.argv[1:])