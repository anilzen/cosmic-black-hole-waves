from helpers import *
# import matplotlib
# matplotlib.use('TKAgg') # This replaces the macosx backend if needed.
import matplotlib.pyplot as plt
import matplotlib.animation as anim
# from pylab import * # For Matlab style animation

# The grid
n = 251                  # spatial grid points
x = np.linspace(0, 1, n)     # the grid
hgx = 1./(n-1)           # spatial grid spacing
hgt = 0.05               # time step

endtime = 300           # end time, eh...
tds = 10                # downsampling in time
nsteps = int(endtime/tds/hgt)  # number of time steps

# Initial data
x0 = 0.5
sigma = 0.02
initial = np.zeros((2, len(x)))
initial[1, :] = gaussian(x, x0, sigma)

# Coefficients
ell = 2  # the spherical harmonic mode (ell<2 is unstable for gravitation)
coefs = set_coefs(x, ell)

# Solve the wave equation
data = wave1dsolve(initial, coefs, hgx, hgt, tds, nsteps)

################################################################
# Animate the solution proper matplotlib style
################################################################

# Setup figure and subplots
fig = plt.figure(figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
plt.tight_layout()

# Set titles and text
ax1.set_title('Evolution of u and u_t')
time_template = 'time = %.1f'
time_text = ax1.text(0.05, 0.9, '', transform=ax1.transAxes)
ax2.set_title('Measurement of log|u| along null infinity')
plt.subplots_adjust(hspace=0.27, top=0.95, left=0.1)

# Set label names
ax1.set_xlabel(r'$\rho$')
ax1.set_ylabel(r'$(u, u_t)$')
ax2.set_xlabel(r'$t$')
ax2.set_ylabel(r'$\log|u|$')

# Turn on grids
ax1.grid(True)
ax2.grid(True)

# Set plots
cur = data[0, :, :]
l11, = ax1.plot(x, cur[0, :], 'b-', label='u')
l12, = ax1.plot(x, cur[1, :], 'r-', label='u_t')
l2,  = ax2.semilogy([], [], 'k-', label='log|u|')

# Set limits
ax1.set_xlim(0, 1)
mx = abs(cur).max()
ax1.set_ylim(-1.05*mx, 1.05*mx)
ax2.set_xlim(0, 5)  # endtime)
ax2.set_ylim(1e-7, 10)

# Set legends
ax1.legend()
ax2.legend()

# Update data
xdata, ydata = [], []


def animate(i):
    t = i*hgt*tds
    cur = data[i, :, :]
    # ax1
    mx = abs(cur).max()
    ax1.set_ylim(-1.05*mx, 1.05*mx)
    l11.set_ydata(cur[0, :])
    l12.set_ydata(cur[1, :])
    time_text.set_text(time_template % (t))
    # ax2
    xdata.append(t)
    ydata.append(abs(cur[0, -1]))
    xmin, xmax = ax2.get_xlim()
    if t > xmax:
        ax2.set_xlim(xmin, 2*xmax)
        ax2.figure.canvas.draw()
    l2.set_data(xdata, ydata)
    return l11, l12, l2, time_text


ani = anim.FuncAnimation(fig, animate, np.arange(len(data)), blit=False,
                         interval=1, repeat=False)

plt.show()


################################################################
# Alternative Matlab style animation method
################################################################
# slowdown=0.002
# ion()
# figure(figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
# # The graph of the wave function (real parts of u and h * u_t)
# # subplot(1,1,1)
# cur=data[0,:,:]
# line1,=plot(x,cur[0,:], 'b-',label='u')
# line2,=plot(x,cur[1,:], 'r-',label='u_t')
# mx = abs(cur).max()
# ylim(-1.05*mx,1.05*mx)
# title("time = %0.2f" % 0.0)
# legend()
# draw()
# show()
# pause(slowdown)
# for i in range(1,nsteps):
#     cur=data[i,:,:]
#     time=i*hgt*tds
#     mx = abs(cur).max()
#     title("time = %0.2f" % time)
#     ylim(-1.05*mx,1.05*mx)
#     line1.set_ydata(cur[0,:])
#     line2.set_ydata(cur[1,:])
#     draw()
#     show()
#     pause(slowdown)
# # For persistent plot for last time step
# ioff()
# cur=data[-1,:,:]
# time=nsteps*hgt*tds
# mx = abs(cur).max()
# title("time = %0.2f" % time)
# ylim(-1.05*mx,1.05*mx)
# line1.set_ydata(cur[0,:])
# line2.set_ydata(cur[1,:])
# draw()
# show()
