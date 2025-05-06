'''
将visualize中的内容改为使用plotly之类可以交互式的图表展示

可以是渲染一个页面 鼠标移动可以看到曲线上具体的值

'''

from first_try import my_fun
import plotly.graph_objects as go
import os

# 创建输出目录
os.makedirs('./output', exist_ok=True)

# 建立映射关系
y_dict = {}
for x in range(1001, 10000):
    if x % 1111 != 0:  # 跳过全同数字
        y_dict[x] = my_fun(x)

max_times = 10

# 创建图表
fig = go.Figure()

# 绘制所有轨迹
for x, y in y_dict.items():
    # 记录迭代轨迹
    trajectory = [x]
    current = x
    for _ in range(max_times):  # 最多迭代4次
        current = y_dict.get(current, current)
        trajectory.append(current)
    
    # 添加轨迹线
    fig.add_trace(go.Scatter(
        x=list(range(len(trajectory))),
        y=trajectory,
        mode='lines',
        line=dict(color='blue', width=0.5),
        name=f'Start: {x}',
        hovertemplate='Iteration: %{x}<br>Value: %{y}<extra></extra>'
    ))

# 设置图表布局
fig.update_layout(
    title='6174 Problem: All Trajectories',
    xaxis_title='Iteration Count',
    yaxis_title='Number Value',
    showlegend=False,
    hovermode='x unified'
)

# 保存为HTML文件
fig.write_html('./output/visualize_interactive.html')

# 显示图表
fig.show()