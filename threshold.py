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
    func = lambda x: 0 if x > threshold else 255
    return filters.threshold_adaptive(img, 1, 'generic', param=func)
    
def randomThresholding(img, amplitude):
    noise_mat = np.random.uniform(0, amplitude, (img.shape[0], img.shape[1]))
    img_noised = img + noise_mat
    func = lambda x: 0 if x > 0.5 else 255
    return filters.threshold_adaptive(img_noised, 1, 'generic', param=func)

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
    