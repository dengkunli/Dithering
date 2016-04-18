
from skimage import io, color, filters
import threshold, random


img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)



bin_image_fixed = threshold.fixedThresholding(img_gray, 120/255)
io.imshow(bin_image_fixed)

bin_image_random = threshold.randomThresholding(img_gray, 0.3)
io.imshow(bin_image_random)

