import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置窗口大小
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 设置颜色
RED = (255, 0, 0)

# 设置正方形初始位置
square_size = 20
square_x = width // 2 - square_size // 2
square_y = height // 2 - square_size // 2

# 设置帧率
clock = pygame.time.Clock()
fps = 60

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_y -= 10
    if keys[pygame.K_s]:
        square_y += 10
    if keys[pygame.K_a]:
        square_x -= 10
    if keys[pygame.K_d]:
        square_x += 10
    if keys[pygame.K_r]:  # 当按下r键时，正方形回到中心
        square_x = width // 2 - square_size // 2
        square_y = height // 2 - square_size // 2

    # 填充背景色
    screen.fill((0, 0, 0))

    # 绘制正方形
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(fps)

# 退出游戏
pygame.quit()
sys.exit()
