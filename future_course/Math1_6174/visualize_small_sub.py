'''
# 验证6174问题
我们已经实现了my_fun，可以from first_try import my_fun 载入

建立一个int 到int的map，来存储y = my_fun(x)的映射关系

我想找一些15个x，这15个x会映射到8个y，然后绘制一下A到B的映射关系

可视化保存在./15_to_8.jpg
'''

from first_try import my_fun
import matplotlib.pyplot as plt
from collections import defaultdict
import random

# 遍历所有四位数，找到8个不同的y值
y_to_x = defaultdict(list)
random_order_x_values = list(range(1000, 10000))
random.shuffle(random_order_x_values)
for x in random_order_x_values:
    y = my_fun(x)
    y_to_x[y].append(x)
    # if len(y_to_x) == 8 and all(len(v) >= 2 for v in y_to_x.values()):
    #     break

# 选择至少15个x值
x_values = []
for y, x_list in y_to_x.items():
    x_values.extend(x_list[:2])  # 每个y值至少取2个x值
x_values = x_values[:15]  # 确保总共有15个x值

# 计算对应的y值
y_values = [my_fun(x) for x in x_values]

# 建立x到y的映射关系
mapping = dict(zip(x_values, y_values))

# 绘制映射关系图
plt.figure(figsize=(6, 12))
# set font size
plt.rcParams.update({'font.size': 16})

for x, y in mapping.items():
    plt.plot([0, 1], [x, y], marker='o', linestyle='-', markersize=8)
    plt.text(1, y, str(y), fontsize=9, ha='left', va='bottom')
    plt.text(0, x, str(x), fontsize=9, ha='right', va='top')


plt.xlim((-0.1, 1.1))
plt.title('6174 Problem: Mapping from X to Y')
plt.xticks([])
plt.yticks([])
plt.grid(True)

# 保存可视化结果
plt.savefig('./15_to_8.jpg')
plt.show()

