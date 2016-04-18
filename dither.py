
from skimage import io, color, filters
img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)


def fixedThresholding(img, threshold):
    func=lambda x: 0 if x > threshold else 255
    return filters.threshold_adaptive(img, 1, 'generic', param=func)

bin_image_fixed = fixedThresholding(img_gray, 120/255)
io.imshow(bin_image_fixed)

