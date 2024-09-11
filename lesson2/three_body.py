import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 常量定义
G = 1  # 简化引力常数
M = 1  # 三个天体的质量相等

# 初始条件
r1 = np.array([0.5, 0.5])  # 天体1的位置
r2 = np.array([-0.5, -0.5])  # 天体2的位置
r3 = np.array([-0.5, 0.5])  # 天体3的位置

v1 = np.array([0, 0.5])  # 天体1的速度
v2 = np.array([0, -0.5])  # 天体2的速度
v3 = np.array([0.5, 0])  # 天体3的速度

def force(r1, r2):
    """计算两个天体之间的引力"""
    r = r2 - r1
    distance = np.linalg.norm(r)
    if distance == 0:
        return np.zeros(2)
    return G * M * M * r / distance**3

def derivatives(r1, r2, r3, v1, v2, v3):
    """计算位置和速度的导数"""
    dr1dt = v1
    dr2dt = v2
    dr3dt = v3
    
    dv1dt = force(r1, r2) + force(r1, r3)
    dv2dt = force(r2, r1) + force(r2, r3)
    dv3dt = force(r3, r1) + force(r3, r2)
    
    return dr1dt, dr2dt, dr3dt, dv1dt, dv2dt, dv3dt

def rk4_step(r1, r2, r3, v1, v2, v3, dt):
    """四阶龙格库塔方法"""
    dr1dt1, dr2dt1, dr3dt1, dv1dt1, dv2dt1, dv3dt1 = derivatives(r1, r2, r3, v1, v2, v3)
    
    r1_2 = r1 + dr1dt1 * dt / 2
    r2_2 = r2 + dr2dt1 * dt / 2
    r3_2 = r3 + dr3dt1 * dt / 2
    v1_2 = v1 + dv1dt1 * dt / 2
    v2_2 = v2 + dv2dt1 * dt / 2
    v3_2 = v3 + dv3dt1 * dt / 2
    
    dr1dt2, dr2dt2, dr3dt2, dv1dt2, dv2dt2, dv3dt2 = derivatives(r1_2, r2_2, r3_2, v1_2, v2_2, v3_2)
    
    r1_3 = r1 + dr1dt2 * dt / 2
    r2_3 = r2 + dr2dt2 * dt / 2
    r3_3 = r3 + dr3dt2 * dt / 2
    v1_3 = v1 + dv1dt2 * dt / 2
    v2_3 = v2 + dv2dt2 * dt / 2
    v3_3 = v3 + dv3dt2 * dt / 2
    
    dr1dt3, dr2dt3, dr3dt3, dv1dt3, dv2dt3, dv3dt3 = derivatives(r1_3, r2_3, r3_3, v1_3, v2_3, v3_3)
    
    r1_4 = r1 + dr1dt3 * dt
    r2_4 = r2 + dr2dt3 * dt
    r3_4 = r3 + dr3dt3 * dt
    v1_4 = v1 + dv1dt3 * dt
    v2_4 = v2 + dv2dt3 * dt
    v3_4 = v3 + dv3dt3 * dt
    
    dr1dt4, dr2dt4, dr3dt4, dv1dt4, dv2dt4, dv3dt4 = derivatives(r1_4, r2_4, r3_4, v1_4, v2_4, v3_4)
    
    r1_new = r1 + (dr1dt1 + 2*dr1dt2 + 2*dr1dt3 + dr1dt4) * dt / 6
    r2_new = r2 + (dr2dt1 + 2*dr2dt2 + 2*dr2dt3 + dr2dt4) * dt / 6
    r3_new = r3 + (dr3dt1 + 2*dr3dt2 + 2*dr3dt3 + dr3dt4) * dt / 6
    
    v1_new = v1 + (dv1dt1 + 2*dv1dt2 + 2*dv1dt3 + dv1dt4) * dt / 6
    v2_new = v2 + (dv2dt1 + 2*dv2dt2 + 2*dv2dt3 + dv2dt4) * dt / 6
    v3_new = v3 + (dv3dt1 + 2*dv3dt2 + 2*dv3dt3 + dv3dt4) * dt / 6
    
    return r1_new, r2_new, r3_new, v1_new, v2_new, v3_new

# 模拟参数
dt = 0.01  # 时间步长
steps = 1000  # 时间步数

# 初始化位置和速度的存储
r1_list, r2_list, r3_list = [], [], []

for _ in range(steps):
    r1, r2, r3, v1, v2, v3 = rk4_step(r1, r2, r3, v1, v2, v3, dt)
    r1_list.append(r1)
    r2_list.append(r2)
    r3_list.append(r3)

# 转换为numpy数组以便绘图
r1_list = np.array(r1_list)
r2_list = np.array(r2_list)
r3_list = np.array(r3_list)

# 创建动画
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Three-Body Problem Simulation')
ax.grid(True)

body1, = ax.plot([], [], 'ro')
body2, = ax.plot([], [], 'go')
body3, = ax.plot([], [], 'bo')
trail1, = ax.plot([], [], 'r-', lw=0.5)
trail2, = ax.plot([], [], 'g-', lw=0.5)
trail3, = ax.plot([], [], 'b-', lw=0.5)

def init():
    body1.set_data([], [])
    body2.set_data([], [])
    body3.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    trail3.set_data([], [])
    return body1, body2, body3, trail1, trail2, trail3

def update(frame):
    body1.set_data(r1_list[frame, 0], r1_list[frame, 1])
    body2.set_data(r2_list[frame, 0], r2_list[frame, 1])
    body3.set_data(r3_list[frame, 0], r3_list[frame, 1])
    trail1.set_data(r1_list[:frame, 0], r1_list[:frame, 1])
    trail2.set_data(r2_list[:frame, 0], r2_list[:frame, 1])
    trail3.set_data(r3_list[:frame, 0], r3_list[:frame, 1])
    return body1, body2, body3, trail1, trail2, trail3

ani = FuncAnimation(fig, update, frames=range(steps), init_func=init, blit=True, interval=20)

plt.show()
