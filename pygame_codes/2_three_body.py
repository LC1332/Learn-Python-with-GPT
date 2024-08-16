
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 基本常数
G = 6.67430e-11  # 引力常数, m^3 kg^-1 s^-2

# 行星属性：质量 (m), 位置 (x, y), 速度 (vx, vy)
bodies = [
    {'m': 5.972e24, 'x': 0, 'y': 0, 'vx': 0, 'vy': 0},   # 地球
    {'m': 7.348e22, 'x': 3.844e8, 'y': 0, 'vx': 0, 'vy': 2.9783e4},  # 月球
    {'m': 1.989e30, 'x': 1.496e11, 'y': 0, 'vx': 0, 'vy': 3.0287e4},  # 太阳
]

# 时间步长
dt = 86400  # 一天

# 模拟时间
t_max = 30 * dt  # 模拟30天

# 初始化轨迹列表
trajectories = {i: {'x': [body['x']], 'y': [body['y']]} for i, body in enumerate(bodies)}

# Euler方法更新位置和速度
def update_bodies(bodies, dt):
    for i, body_i in enumerate(bodies):
        # 计算引力
        for j, body_j in enumerate(bodies):
            if i != j:
                # 两物体之间的距离
                dx = body_j['x'] - body_i['x']
                dy = body_j['y'] - body_i['y']
                r = np.sqrt(dx**2 + dy**2)
                
                # 引力加速度
                f = G * body_i['m'] * body_j['m'] / r**2
                ax = f * dx / r
                ay = f * dy / r
                
                # 更新速度和位置
                body_i['vx'] += ax * dt
                body_i['vy'] += ay * dt
                body_i['x'] += body_i['vx'] * dt
                body_i['y'] += body_i['vy'] * dt

                # 记录轨迹
                trajectories[i]['x'].append(body_i['x'])
                trajectories[i]['y'].append(body_i['y'])

# 进行模拟
time = 0
while time < t_max:
    update_bodies(bodies, dt)
    time += dt

# 可视化
def animate(i):
    plt.clf()
    for body in bodies:
        plt.scatter(body['x'], body['y'], color='blue')
    for i, trajectory in trajectories.items():
        plt.plot(trajectory['x'][:i+1], trajectory['y'][:i+1], color='green')
    plt.xlim(min(trajectory['x']) - 1e8, max(trajectory['x']) + 1e8)
    plt.ylim(min(trajectory['y']) - 1e8, max(trajectory['y']) + 1e8)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('三体运动模拟')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

ani = FuncAnimation(plt.gcf(), animate, frames=len(trajectories[0]['x']) - 1, interval=50)
plt.show()
