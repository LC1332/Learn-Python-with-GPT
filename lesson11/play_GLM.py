import pygame
import pymunk

# 初始化pygame
pygame.init()

# 设置屏幕大小和标题
width, height = 100, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pymunk Physics Simulation")

# 设置时钟
clock = pygame.time.Clock()

# 创建pymunk空间
space = pymunk.Space()
space.gravity = (0, 900)  # 设置重力为y正方向

# 定义杯子墙壁
cup_thickness = 0
static_lines = [
    pymunk.Segment(space.static_body, (0, cup_thickness), (0, height), cup_thickness),
    pymunk.Segment(space.static_body, (width, cup_thickness), (width, height), cup_thickness),
    pymunk.Segment(space.static_body, (0, height), (width, height), cup_thickness),
]
for line in static_lines:
    line.elasticity = 0.0  # 完全非弹性碰撞
    space.add(line)  # 逐个添加到空间中

# 小球半径
radius = 8

import random

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # 在杯口生成小球
            ball_mass = 10
            ball_moment = pymunk.moment_for_circle(ball_mass, 0, radius)
            ball_body = pymunk.Body(ball_mass, ball_moment)
            # sample x from radius to width - radius
            x = radius + cup_thickness + random.uniform(0, width - 2 * radius - cup_thickness)
            # ball_body.position = (radius + cup_thickness, radius)
            ball_body.position = (x, radius)
            ball_shape = pymunk.Circle(ball_body, radius)
            ball_shape.elasticity = 1.0  # 完全非弹性碰撞
            # set elasticity to 0.0
            ball_shape.elasticity = 0.0
            space.add(ball_body, ball_shape)

    # 更新pymunk空间
    space.step(1/50.0)

    # 绘制背景
    screen.fill((255, 255, 255))

    # 绘制小球
    for ball in space.shapes:
        if isinstance(ball, pymunk.Circle):
            pos = ball.body.position
            pygame.draw.circle(screen, (0, 0, 255), pos.int_tuple, int(ball.radius))

    # 更新屏幕
    pygame.display.flip()

    # 设置帧率
    clock.tick(50)

# 退出pygame
pygame.quit()
