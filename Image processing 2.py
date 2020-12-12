from PIL import Image
import numpy as np
from skimage.util import random_noise

im = Image.open("sample.jpg")
im_arr = np.asarray(im)

noise_img = random_noise(im_arr, mode='gaussian', var=0.05**2)
noise_img = (500*noise_img).astype(np.uint8)

img = Image.fromarray(noise_img)
img.show()
