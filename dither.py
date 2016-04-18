from skimage import io, color, filters 
img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)
io.imshow(img_gray)

binary_image1 = filters.threshold_adaptive(img_gray, 15, 'gaussian')
io.imshow(binary_image1)