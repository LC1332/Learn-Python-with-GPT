'''
# 6174问题可视化
我们已经实现了my_fun，可以from first_try import my_fun 载入
建立一个int 到int的map，来存储y = my_fun(x)的映射关系
再建立一个int 到 list of int的map，inv_fun 来存储x到y的关系
定义 (6174,0)，表示6174可以通过0次操作，就到达6174
如果一个数x的位置在(x, i)，就说明x可以通过i次操作，到达6174
我想绘制所有的0到9998的点的位置，并且如果一个(x,i)可以到达(y,i-1)就用蓝色细线连接起来
结果保存在output/visualize_tree.jpg
'''

from first_try import my_fun
import matplotlib.pyplot as plt
from collections import defaultdict
import os

# 创建输出目录
os.makedirs('./output', exist_ok=True)

# 建立映射关系
y_dict = {}
inv_dict = defaultdict(list)

# 遍历所有四位数
for x in range(1, 10000):
    if x % 1111 != 0:  # 跳过全同数字
        y = my_fun(x)
        y_dict[x] = y
        inv_dict[y].append(x)

# 计算每个数字到达6174所需的步数
steps_dict = {}
queue = [(6174, 0)]
while queue:
    num, step = queue.pop(0)
    if num in steps_dict:
        continue
    steps_dict[num] = step
    for x in inv_dict[num]:
        queue.append((x, step + 1))

print("finished search, len y_dict =", len(y_dict))

# 绘制树状图
plt.figure(figsize=(20, 10))

from tqdm import tqdm
for x, y in tqdm(y_dict.items()):
    if x == 6174:
        continue
    # 绘制连接线
    plt.plot([-steps_dict[x], -steps_dict[y]], [x, y], 
             color='blue', linewidth=0.5, alpha=0.5)
    # 绘制点
    # plt.scatter(steps_dict[x], x, color='red', s=5)
    # plt.scatter(steps_dict[y], y, color='red', s=5)

# 设置图表属性
plt.title('6174 Problem: Tree Visualization')
plt.xlabel('Steps to 6174')
plt.ylabel('Number Value')
plt.grid(True)

# 保存图像
plt.savefig('./output/visualize_tree.jpg')
plt.show()

