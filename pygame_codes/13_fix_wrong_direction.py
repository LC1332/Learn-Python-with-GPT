import pymunk
import pygame
import sys

# 初始化pygame
pygame.init()

# 设置屏幕大小
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

# 设置时钟
clock = pygame.time.Clock()

# 创建一个空间
space = pymunk.Space()
# space.gravity = (0, 981)  # 设置重力，向下
# 手工修改
space.gravity = (0, - 981)  # 设置重力，向下


# 杯子的尺寸
cup_width = 100
cup_height = 300
cup_x = 50  # 杯子左侧的x坐标
cup_y = height - 50  # 杯子底部的y坐标

# 创建杯子的墙壁
static_lines = [
    pymunk.Segment(space.static_body, (cup_x, cup_y), (cup_x, cup_y - cup_height), 5),
    pymunk.Segment(space.static_body, (cup_x, cup_y - cup_height), (cup_x + cup_width, cup_y - cup_height), 5),
    pymunk.Segment(space.static_body, (cup_x + cup_width, cup_y - cup_height), (cup_x + cup_width, cup_y), 5)
]

for line in static_lines:
    line.elasticity = 0.5
    line.friction = 0.5
    space.add(line)

# 渲染函数
def draw(space):
    screen.fill((255, 255, 255))
    
    # 绘制墙壁
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(screen, (0, 0, 0), False, [p1, p2])

    # 绘制小球
    for ball in balls:
        pos = ball.body.position
        pygame.draw.circle(screen, (0, 0, 255), to_pygame(pos), int(ball.radius), 2)

    pygame.display.flip()

# 将pymunk坐标转换为pygame坐标
def to_pygame(p):
    return int(p.x), int(-p.y + height)

# 主循环
balls = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # 在杯口位置添加小球
            mass = 10
            radius = 10
            moment = pymunk.moment_for_circle(mass, 0, radius)
            body = pymunk.Body(mass, moment)
            # body.position = cup_x + cup_width / 2, cup_y - cup_height
            # 手工修改
            body.position = cup_x + cup_width / 2, cup_y
            shape = pymunk.Circle(body, radius)
            shape.elasticity = 0.5
            space.add(body, shape)
            balls.append(shape)

    # 模拟
    space.step(1/50.0)
    
    # 渲染
    draw(space)
    
    # 控制帧率
    clock.tick(50)

pygame.quit()
sys.exit()
