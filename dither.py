from skimage import io, color, filters
import threshold


img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)


bin_image_fixed = threshold.fixedThresholding(img_gray, 120/255)

io.imshow(bin_image_fixed)
