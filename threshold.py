from skimage import filters
import numpy as np

def fixedThresholding(img, threshold):
    func = lambda x: 0 if x > threshold else 255
    return filters.threshold_adaptive(img, 1, 'generic', param=func)
    
def randomThresholding(img, amplitude):
    noise_mat = np.random.uniform(0, amplitude, (img.shape[0], img.shape[1]))
    img_noised = img + noise_mat
    func = lambda x: 0 if x > 0.5 else 255
    return filters.threshold_adaptive(img_noised, 1, 'generic', param=func)