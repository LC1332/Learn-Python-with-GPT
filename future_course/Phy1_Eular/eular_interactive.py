'''
eular_with_resis.py的代码可以顺利运行

我希望能够渲染出一个交互式的页面

vx vy和b的数值可以通过一个slider来控制

拖动后重新显示轨迹
'''

import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

def simulate_trajectory(vx, vy, b):
    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    dt = 0.01  # time step (s)
    
    # Initial conditions
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
    return plt

def update_plot(vx, vy, b):
    plt = simulate_trajectory(vx, vy, b)
    return plt

iface = gr.Interface(
    fn=update_plot,
    inputs=[
        gr.Slider(minimum=0, maximum=100, value=30, label="Horizontal Velocity (vx)"),
        gr.Slider(minimum=0, maximum=100, value=30, label="Vertical Velocity (vy)"),
        gr.Slider(minimum=0, maximum=1, value=0.1, step=0.01, label="Air Resistance Coefficient (b)")
    ],
    outputs="plot",
    live=True
)

if __name__ == "__main__":
    iface.launch()

