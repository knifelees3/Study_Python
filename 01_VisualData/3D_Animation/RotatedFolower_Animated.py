import subprocess
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator


[x, t] = np.meshgrid(np.array(range(25))/24.0,
                     np.arange(0, 575.5, 0.5)/575*17*np.pi-2*np.pi)

p = (np.pi/2)*np.exp(-t/(8*np.pi))

u = 1-(1-np.mod(3.6*t, 2*np.pi)/np.pi)**4/2

y = 2*(x**2-x)**2*np.sin(p)

r = u*(x*np.sin(p)+y*np.cos(p))

fig = plt.figure()
ax = Axes3D(fig)


def init():

    surf = ax.plot_surface(r*np.cos(t), r*np.sin(t), u*(x*np.cos(p)-y*np.sin(p)),
                           rstride=1, cstride=1, cmap=cm.gist_rainbow_r, linewidth=0, antialiased=True)
    plt.axis('off')
    return fig,


def animate(i):
    # azimuth angle : 0 deg to 360 deg
    ax.view_init(elev=10, azim=i*4)
    return fig,


# Animate
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=90, interval=50, blit=True)


fn = 'rotate_azimuth_angle_3d_flower'
# ani.save(fn+'.mp4',writer='ffmpeg',fps=1000/50)
ani.save(fn+'.gif', writer='imagemagick', fps=1000/50)

cmd = 'magick convert %s.gif -fuzz 5%% -layers Optimize %s_r.gif' % (fn, fn)
subprocess.check_output(cmd)


plt.rcParams['animation.html'] = 'html5'
ani
