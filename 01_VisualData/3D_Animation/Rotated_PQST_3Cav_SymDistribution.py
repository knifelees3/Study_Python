# As a study of 3D data visualization using Python package Mayavi
# Author Zhaohua Tian
# Email:knifelees3@gmail.com
# I will show the figures in the Ref: "Quantum photonic node for on-chip state transfer" (https://arxiv.org/abs/1908.03683)
# The original figures are plotted via MATLAB and the 3d data visualization is not suitable for using Matplotlib.
# In this note I try to replot the data and let it rotated


# %%
import numpy as np
from mayavi import mlab
import moviepy.editor as mpy
# %% Load the data
dis_tri = np.loadtxt('BigRangeSweep3Cav.txt')
# %%
num_J12 = 199
num_J23 = 200
num_kappa = 201
J12_mat = np.linspace(1, 9, num_J12)
J23_mat = np.linspace(1, 10, num_J23)
kappa_mat = np.linspace(1, 14, num_kappa)

# %% reshape the data
sym_mat = np.reshape(dis_tri, (num_kappa, num_J23, num_J12))
sym_mat = sym_mat.transpose(1, 2, 0)
xx, yy, zz = np.mgrid[1:10:200j, 1:9:199j, 1:14:201j]

# %%
fig_extent = [1, 10, 1, 9, 1, 14]
fig1 = mlab.figure(size=(800, 800), bgcolor=(1, 1, 1), fgcolor=(0, 0, 0))
mlab.contour3d(xx, yy, zz, sym_mat, color=(0, 0.3, 0.3), contours=[
    0.8], transparent=True, opacity=0.15)  # ,extent=fig_extent)
mlab.contour3d(xx, yy, zz, sym_mat, color=(0, 0.7, 0.7), contours=[
               0.9], transparent=True, opacity=0.3)  # ,extent=fig_extent)
mlab.contour3d(xx, yy, zz, sym_mat, color=(0, 0, 0.8), contours=[
               0.97], transparent=True, opacity=0.4)  # ,extent=fig_extent)
mlab.outline(extent=fig_extent)
mlab.axes(color=(1, 0, 0), nb_labels=5)
# mlab.xlabel('J23/g')
# mlab.ylabel('J12/g')
# mlab.zlabel('K/2g')
# mlab.show()


def make_frame(t):
    # camera angle
    mlab.view(azimuth=360 * t / duration, elevation=-70, distance=42, focalpoint=[5.5, 5, 7.5])
    return mlab.screenshot(antialiased=True)


duration = 5
animation = mpy.VideoClip(make_frame, duration=duration).resize(0.5)
# # Video generation takes 10 seconds, GIF generation takes 25s
# #animation.write_videofile("Rotated_sym_distri_static_Python.mp4", fps=20)
animation.write_gif("Rotated_sym_distri_static_Python.gif", fps=20)
mlab.close(fig1)

# %%
