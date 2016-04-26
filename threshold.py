from skimage import filters
import numpy as np

def createFilter(mat, shape):
    s = np.tile(mat, (np.ceil(shape[0]/mat.shape[0]), np.ceil(shape[1]/mat.shape[1])))
    return np.resize(s, shape) + 0.5

def quantification(img, level):
    return img * level / 255

def threshold(img, s):
    res = np.zeros( img.shape, dtype=int )
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] > s[i][j]:
                res[i][j] = 1
    return res            

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

'''
The filter of Floyd & Steinberg
F=| 0 0 7|*(1/16)
  | 3 5 1|
'''
def errorDiffusion(img_grey):
    #Creat a new variable "img" so that when we excute the funcion, the original variable "img_grey" will not be affected.
    img=img_grey.copy()
    #From left to right and from top to bottom, apply the filter pixel by pixel
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


clustered_dots = np.array(
                [[34, 25, 21, 17, 29, 33],
                 [30, 13, 9 , 5 , 12, 24],
                 [18, 6 , 1 , 0 , 8 , 20],
                 [22, 10, 2 , 3 , 4 , 16],
                 [26, 14, 7 , 11, 15, 28],
                 [35, 31, 19, 23, 27, 32]])

# img: 255 grays
def orderedThreshold(img, mat):
    s = createFilter(mat, img.shape)
    q = quantification(img, mat.size)
    return threshold(q, s)
    

