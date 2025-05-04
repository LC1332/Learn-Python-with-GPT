import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
dt = 0.01  # time step (s)
b = 0.1  # air resistance coefficient (N·s²/m²)

# Initial conditions
vx = 30  # horizontal velocity (m/s)
vy = 30  # initial vertical velocity (m/s)
x = 0  # initial horizontal position (m)
y = 10  # initial vertical position (m)

# Time simulation
t_final = 10  # total time of simulation (s)
n_steps = int(t_final / dt)  # number of steps

# Lists to store the trajectory points
x_list = [x]
y_list = [y]

# Simulation loop
for _ in range(n_steps):
    # Calculate the magnitude of velocity
    v = np.sqrt(vx**2 + vy**2)
    
    # Update velocities with air resistance
    vx -= b * v * vx * dt
    vy -= (g + b * v * vy) * dt
    
    # Update positions using the current velocity
    x += vx * dt
    y += vy * dt
    
    # Append the new positions to the lists
    x_list.append(x)
    y_list.append(y)
    
    # Stop if the ball hits the ground
    if y <= 0:
        break

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x_list, y_list, marker='o')
plt.title('Projectile Motion Trajectory with Air Resistance')
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.grid(True)
plt.show()
