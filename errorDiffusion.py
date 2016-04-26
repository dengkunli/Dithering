import numpy as np

# Floyd & Steinberg filter
F1 = np.array([[0,0,7],
               [3,5,1]])
F1 = 1/F1.sum() * F1

# Stucki filter
F2 = np.array([[0,0,0,8,4],
               [2,4,8,4,2],
               [1,2,4,2,1]])
F2 = 1/F2.sum() * F2

# main function
#   input:
#       img: gray-scale image, 256 levels of grays, normalized to [0, 1]
#       filterName: name of the filter to be applied
#   output:
#       out: output image processed by error diffusion
def process(img, filterName):
    if filterName == "FloydSteinberg":
        F = F1
    elif filterName == "Stucki":
        F = F2
    else:
        F = F1
    threshold = 0.5
    out = np.zeros(img.shape)
    padDim1 = (0, F.shape[0] - 1)
    padDim2 = ( np.int(np.floor(F.shape[1]/2)), np.int(np.floor(F.shape[1]/2)) )
    I = np.lib.pad(img, (padDim1,padDim2), 'constant', constant_values=0)
    for y in range(padDim2[0], I.shape[1]-padDim2[1]):
        for x in range(0, I.shape[0]-padDim1[1]):
            ox = x
            oy = y - padDim2[0]

            # set the value in the corresponding pixel
            out[ox][oy] = I[x][y] > threshold

            # calculate the error
            error = I[x][y] - out[ox][oy]

            # get the block where the filter should be applied
            xmin = x
            xmax = x + F.shape[0] - 1
            ymin = y - np.int(np.floor(F.shape[1]/2))
            ymax = y + np.int(np.floor(F.shape[1]/2))

            # distribute the error
            I[xmin:xmax+1,ymin:ymax+1] = I[xmin:xmax+1,ymin:ymax+1] + error * F
    return out