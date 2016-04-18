from skimage import io, color, filters
from fixedThresholding import fixedThresholding


img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)


bin_image_fixed = fixedThresholding(img_gray, 120/255)

io.imshow(bin_image_fixed)
