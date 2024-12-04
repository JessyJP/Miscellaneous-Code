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

def initial_setup():
    """
    Sets up the initial figure, axes, line, and point for the animation.
    Returns the figure, axes, line, and point objects.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    line, = ax.plot([], [], [], 'b-', lw=2)
    point, = ax.plot([], [], [], '*r')
    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))
    ax.set_title('Lorenz Attractor')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return fig, ax, line, point

def show_full_plot():
    # Set up the figure and axis for animation
    line, = ax.plot([], [], [], 'b-', lw=2)
    point, = ax.plot([], [], [], '*r')
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    plt.show()
    # TODO: finish this function for to display the full plot


# Solve the Lorenz system
sigma, rho, beta = 10, 28, 8/3
r0 = [1, 1, 1]  # Initial conditions
t_span = [0, 100]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(lorenz_system, t_span, r0, args=(sigma, rho, beta), t_eval=t_eval)

# Setup figure and axes using the initial setup function
fig, ax, line, point = initial_setup()

# Set up video writer
videoFileName = 'LorenzAttractorAnimation.mp4'
writer = FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=1800)
with writer.saving(fig, videoFileName, 100):  # DPI can be adjusted for quality and file size
    for i in range(len(sol.t)):
        # Update the data for line and point with the current frame's data
        line.set_data(sol.y[0, :i+1], sol.y[1, :i+1])
        line.set_3d_properties(sol.y[2, :i+1])
        point.set_data(sol.y[0, i], sol.y[1, i])
        point.set_3d_properties(sol.y[2, i])
        ax.set_title(f'Lorenz Attractor [t = {sol.t[i]:.2f}s]')
        
        # Update the figure on screen
        plt.draw()
        plt.pause(0.001)  # Pause briefly to display the frame
        
        # Grab the current frame and add it to the video
        writer.grab_frame()

print(f"Video saved as {videoFileName}")
