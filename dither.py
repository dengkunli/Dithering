from skimage import io, color, filters
import matplotlib.pyplot as plt
import threshold


img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)

bin_image_fixed = threshold.fixedThresholding(img_gray, 120/255)
plt.figure(1)
plt.imshow(bin_image_fixed, cmap='Greys_r')


bin_image_random = threshold.randomThresholding(img_gray, 0.3)
plt.figure(2)
plt.imshow(bin_image_random, cmap='Greys_r')

