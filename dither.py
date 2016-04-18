from skimage import io, data, color
img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)
io.imshow(img_gray)
