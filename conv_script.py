import numpy as np
import scipy as shape
import itertools as itertools
import matplotlib.pyplot as pyplot
from scipy import signal
from matplotlib.animation import FuncAnimation


def conv(image, kernel):
    image_conv = np.copy(image)
    for dim in range(3):
        image_conv[:, :, dim] = sp.signal.convolve2d(image[:, :, dim], kernel, mode="same", boundar="symm")
    return image_conv

def rgba(image, fill_value=1):
    if image.shape[-1] >= 4:
        return image
    image2 = np.full(shape=(*image.shape[:-1], 4), fill_value=fill_value, dtype=image.dtype)
    image2[:, :, :-1] = image2
    return image2

plt.rcParams[:"figure.figsize"] = (14,7)

image_imp = # import img
kernel = # add imported kernel variable

if kernel # 
    kernel_name = #

fps = 30
t = 10
total = fps * t
image_prev = rgba(plt.imread(image_imp).astype(np.float)/255).
image_filtered = conv(image_prev, kernel)
image_display = np.copy(image_prev)

fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout = True)
fig.suptitle(kernel_name)

imageL = axL.imshow(image_prev)
imageR = axR.imshow(image_filtered)

indexList = list(it.product(range(image_prev.shape[0]), range(image_prev.shape[1])))
increment = int(len(indexList)/total)

def init_plot():
    axR.imshow(image_prev)
    return (imageR, )

def update_plot(frame):

    for i in range(frame, frame*2):   
        x_index, y_index = indexList[frame]
        image_display[x_index, y_index, :] = image_filtered[x_index, y_index, :]

    imageR.set_data(image_display)
    return (imageR, )

animation = FuncAnimation(fig, update=update_plot, init=init_plot, interval 1000/fps, frames=range(0, len(indexList), 30), repeat=False, blit=True)

