import cv2
import numpy as np
import math

if __name__ == "__main__":
    image = cv2.imread("sample.png")
    cv2.imshow("Basic Image", image)
    cv2.waitKey(0)
