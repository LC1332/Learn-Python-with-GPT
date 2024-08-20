import pymunk
import matplotlib.pyplot as plt
from pymunk.vec2d import Vec2d
import openpyxl

# 定义参数
width, height = 100, 300
radius = 8
highest_ball = height
num_balls = 50
space = pymunk.Space()
space.gravity = (0, -981)  # 设置重力

# 定义杯子的墙壁
static_lines = [
    pymunk.Segment(space.static_body, (0, 0), (width, 0), 1),
    pymunk.Segment(space.static_body, (width, 0), (width, height), 1),
    pymunk.Segment(space.static_body, (width, height), (0, height), 1),
]
for line in static_lines:
    line.elasticity = 1.0  # 完全非弹性碰撞

space.add(static_lines)

# 存储小球的高度
ball_heights = []

# 放置小球
for i in range(num_balls):
    # 计算小球位置
    x = width / 2
    y = highest_ball + 5 * radius
    mass = 10
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = x, y
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0  # 完全非弹性碰撞
    space.add(body, shape)
    
    # 模拟一段时间
    for _ in range(50):
        space.step(1/50.0)
    
    # 更新highest_ball
    highest_ball = max(b.position.y for b in space.bodies if isinstance(b.shape, pymunk.Circle))
    ball_heights.append((i, highest_ball))

# 写入Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Ball Heights"
for row in ball_heights:
    ws.append(row)
wb.save("ball_heights.xlsx")

print("Simulation complete. Ball heights have been saved to 'ball_heights.xlsx'.")
