from skimage import filters
def fixedThresholding(img, threshold):
    func = lambda x: 0 if x > threshold else 255
    return filters.threshold_adaptive(img, 1, 'generic', param=func)