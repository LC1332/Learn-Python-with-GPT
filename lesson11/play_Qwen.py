import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

# 创建Pymunk空间
space = pymunk.Space()
space.gravity = (0.0, 900.0)  # 重力方向向下

# 创建杯子的墙壁
static_lines = [
    pymunk.Segment(space.static_body, (50, 600), (50, 300), 0.0),
    pymunk.Segment(space.static_body, (50, 600), (150, 600), 0.0),
    pymunk.Segment(space.static_body, (150, 300), (150, 600), 0.0)
]
for line in static_lines:
    line.elasticity = 0.95
    line.friction = 0.9
# space.add(static_lines)
for line in static_lines:
    space.add(line)

# 用于存放所有动态物体的列表
balls = []

def create_ball(position):
    body = pymunk.Body(10, 1000, body_type=pymunk.Body.DYNAMIC)
    body.position = position
    shape = pymunk.Circle(body, 8)
    shape.elasticity = 0.95
    space.add(body, shape)
    return shape

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_SPACE:
            x = random.randint(58, 142)  # 杯子左边界+radius 到 右边界-radius
            y = 300  # 杯口高度
            balls.append(create_ball((x, y)))

    screen.fill(pygame.Color("white"))

    # 绘制静态线条
    options = pymunk.pygame_util.DrawOptions(screen)
    space.debug_draw(options)

    # 更新物理引擎
    dt = 1.0 / 60.0
    for x in range(1):
        space.step(dt)

    # 绘制动态物体（球）
    for ball in balls:
        p = int(ball.body.position.x), int(ball.body.position.y)
        pygame.draw.circle(screen, pygame.Color("blue"), p, 8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit() 