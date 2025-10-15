import cv2
import numpy as np

def apply_canny_filter(image, lower_t, upper_t, k_size, sigma):
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (k_size, k_size), sigma)
    edges = cv2.Canny(blurred, lower_t, upper_t)
    return edges