import cv2
import numpy as np

def apply_laplacian_filter(image, k_size):
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=k_size)
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian
