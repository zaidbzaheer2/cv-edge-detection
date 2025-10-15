import cv2
import numpy as np

def apply_sobel_filter(image, k_size, direction):
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if direction == "X":
        sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=k_size)
    elif direction == "Y":
        sobel = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=k_size)
    else:
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=k_size)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=k_size)
        sobel = cv2.magnitude(sobel_x, sobel_y)

    sobel = np.uint8(np.absolute(sobel))
    return sobel
