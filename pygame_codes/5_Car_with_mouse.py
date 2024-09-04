import pygame
from Car import Car  # 假设Car类已经在一个名为Car.py的文件中定义

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))

# 创建Car实例
car = Car(50, 50)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
            # 获取鼠标点击的位置
            mouse_x, mouse_y = event.pos
            # 设置Car的目标位置为鼠标点击的位置
            car.set_target(mouse_x, mouse_y)

    # 更新汽车位置
    car.update()

    # 填充背景色
    screen.fill((255, 255, 255))

    # 绘制汽车
    car.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制游戏帧率
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
