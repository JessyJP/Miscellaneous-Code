import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

def lorenz_system(t, r, sigma, rho, beta):
    x, y, z = r
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def show_full_plot():
    # Plot the solution
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol.y[0], sol.y[1], sol.y[2])
    ax.set_title('Lorenz Attractor')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

# Lorenz system parameters
sigma = 10
rho = 28
beta = 8/3

# Initial conditions
r0 = [1, 1, 1]

# Time span for the simulation
t_span = [0, 100]
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the Lorenz system
sol = solve_ivp(lorenz_system, t_span, r0, args=(sigma, rho, beta), t_eval=t_eval)

# Set up the figure and axis for animation
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
line, = ax.plot([], [], [], 'b-', lw=2)
point, = ax.plot([], [], [], '*r')
ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))
ax.set_title('Lorenz Attractor')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')



# Initialization function for the animation
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

# Animation function
def animate(i):
    line.set_data(sol.y[0, :i], sol.y[1, :i])
    line.set_3d_properties(sol.y[2, :i])
    point.set_data(sol.y[0, i], sol.y[1, i])
    point.set_3d_properties(sol.y[2, i])
    return line, point

# Create an animation
from matplotlib.animation import FuncAnimation
anim = FuncAnimation(fig, animate, init_func=init, frames=len(sol.t), interval=30, blit=True)

# Save the animation
writer = FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=1800)
anim.save('LorenzAttractorAnimation.mp4', writer=writer)

plt.show()
