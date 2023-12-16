import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation


def convolve(image_imp, kernel): 
    plt.rcParams["font.size"] = 12

    plt.rcParams["figure.figsize"] = (12, 7)

    
    def conv(image, kern):
        image_conv = np.empty_like(image)
        for dim in range(image.shape[-1]):
            image_conv[:, :, dim] = sp.signal.convolve2d(image_prev[:, :, dim], kern, mode="same", boundary="symm")
        return image_conv
    
    def rgba(image, fill_value=1):
        if image.shape[-1] >= 4:
            return image
        image2 = np.full(shape=(*image.shape[:-1], 4), fill_value=fill_value, dtype=image.dtype)
        image2[:, :, :-1] = image/255.
        return image2
    
    
    fps = 30
    t = 10
    total = fps*t
    
    image_prev = rgba(plt.imread(image_imp).astype(float))
    image_filtered = conv(image_prev, kernel)
    image_filtered[:, :, -1] = 1
    image_display = np.copy(image_prev)
    
    fig, (axL, axR) = plt.subplots(ncols = 2, constrained_layout = True)
    fig.suptitle(kernel)
    
    imL = axL.imshow(image_prev, interpolation="none")
    imR = axR.imshow(image_prev, interpolation="none")
    axR.set_xlim(axL.get_xlim()), axR.set_ylim(axL.get_ylim())
    axL.axis('off'), axR.axis('off')
    imR.set_clim([0, 1])
    
    indexList = list(it.product(range(image_prev.shape[0]), range(image_prev.shape[1])))
    increment = np.int(len(indexList)/total)
    
    def init_plot():
        axR.imshow(image_prev)
        return (imR, )
    
    def update_plot(frame):
    
        for i in range(frame, frame*2):   
            x_index, y_index = indexList[frame]
            image_display[x_index, y_index, :] = image_filtered[x_index, y_index, :]
    
        imR.set_data(image_display)
        return (imR, )

    animation = FuncAnimation(fig, func=update_plot, init_func=init_plot, interval=1000/fps, frames=range(0, len(indexList), increment), repeat=False, blit=True)
    plt.show()
