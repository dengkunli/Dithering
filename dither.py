
from skimage import io, color, filters
import threshold, random


img = io.imread("lenna.png")
img_gray = color.rgb2gray(img)


def fixedThresholding(img, threshold):
    func=lambda x: 0 if x > threshold else 255
    return filters.threshold_adaptive(img, 1, 'generic', param=func)


bin_image_fixed = threshold.fixedThresholding(img_gray,threshold)

io.imshow(bin_image_fixed)

print ("random() : ", random.random())