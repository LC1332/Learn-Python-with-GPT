'''
# 6174问题可视化
我们已经实现了my_fun，可以from first_try import my_fun 载入
建立一个int 到int的map，来存储y = my_fun(x)的映射关系
先建立一个y_dict, y_dict[x]来记录 my_fun(x) 的值
之后我希望用蓝色细线画出每一个非全同四位数，经过若干次迭代的轨迹，横轴是迭代次数最大是10
纵轴是1-9998
保存在./output/visualize_all.jpg
'''


from first_try import my_fun
import matplotlib.pyplot as plt
import os

# 创建输出目录
os.makedirs('./output', exist_ok=True)

# 建立映射关系
y_dict = {}
for x in range(1000, 10000):
    if x % 1111 != 0:  # 跳过全同数字
        y_dict[x] = my_fun(x)

max_times = 10

# 绘制所有轨迹
plt.figure(figsize=(10, 8))
for x, y in y_dict.items():
    # 记录迭代轨迹
    trajectory = [x]
    current = x
    for _ in range(max_times):  # 最多迭代4次
        current = y_dict.get(current, current)
        trajectory.append(current)
    
    # 绘制蓝色细线
    plt.plot(range(len(trajectory)), trajectory, color='blue', linewidth=0.5)

# 设置图表属性
plt.title('6174 Problem: All Trajectories')
plt.xlabel('Iteration Count')
plt.ylabel('Number Value')
plt.xticks(range(5))
plt.grid(True)

# 保存图像
plt.savefig('./output/visualize_all.jpg')
plt.show()

