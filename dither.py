from skimage import io, color, filters
import matplotlib.pyplot as plt
import threshold
import errorDiffusion

# read lenna image
img = io.imread("lenna.png")
# transform to gray-scale, ranging [0, 1]
img_gray = color.rgb2gray(img)

# original gray-scale image
fig0 = plt.figure(0)
fig0.suptitle('original gray image', fontsize=20)
plt.imshow(img_gray, cmap="Greys_r")

# fixed thresholding demo
bin_image_fixed = threshold.fixedThresholding(img_gray, 120/255)
fig1 = plt.figure(1)
fig1.suptitle('fixed thresholding demo', fontsize=20)
plt.imshow(bin_image_fixed, cmap='Greys_r')

# random thresholding demo
bin_image_random = threshold.randomThresholding(img_gray, 0.3)
fig2 = plt.figure(2)
fig2.suptitle('random thresholding demo', fontsize=20)
plt.imshow(bin_image_random, cmap='Greys_r')

# error diffusion demo
#   demo 1: Floyd & Steinberg filter
#   demo 2: Stucki filter
diffused_image_floyd_steinberg = errorDiffusion.process(img_gray, "FloydSteinberg")
diffused_image_stucki = errorDiffusion.process(img_gray, "Stucki")
fig3 = plt.figure(3)
fig3.suptitle('Error Diffusion: Floyd & Steinberg filter', fontsize=20)
plt.imshow(diffused_image_floyd_steinberg, cmap='Greys_r')
fig4 = plt.figure(4)
fig4.suptitle('Error Diffusion: Stucki filter', fontsize=20)
plt.imshow(diffused_image_stucki, cmap='Greys_r')