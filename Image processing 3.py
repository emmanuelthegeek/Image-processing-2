from PIL import Image
import numpy as np
import random
import cv2

im = Image.open("sample.jpg")
# convert to ndarray
im_arr = np.asarray(im)

def sp_noise(image,prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('sample.jpg',0) # Only for grayscale image
noise_img = sp_noise(image,0.05)
print(noise_img)

