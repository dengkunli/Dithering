from skimage import filters
import numpy as np

def fixedThresholding(img, threshold):
    #func = lambda x: 0 if x>threshold else 255
    def func(x):
        if x > threshold:
            return 0
        else:
            return 255
            
    return filters.threshold_adaptive(img, 1, 'generic', param=func)
    
def randomThresholding(img, amplitude):
    noise_mat = np.random.uniform(0, amplitude, (img.shape[0], img.shape[1]))
    #numpy.random.uniform(minValue=0.0, maxValue=amplitude, size=imgLine*imgColone)
    img_noised = img + noise_mat
    func = lambda x: 0 if x > 0.5 else 255
    return filters.threshold_adaptive(img_noised, 1, 'generic', param=func)
    
def errerDiffusion(img):
    for y in range(0, img.shape[1]-1):
        for x in range(1, img.shape[0]-1):
          oldpixel = img[x, y]
          img[x, y] = 1 if oldpixel > 0.5 else 0
          quant_error = oldpixel - img[x, y]
          img[x+1, y  ] = img[x+1, y  ] + 7/16.0 * quant_error
          img[x-1, y+1] = img[x-1, y+1] + 3/16.0 * quant_error
          img[x,   y+1] = img[x,   y+1] + 5/16.0 * quant_error
          img[x+1, y+1] = img[x+1, y+1] + 1/16.0 * quant_error
    
    return img