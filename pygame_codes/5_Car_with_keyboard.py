import pygame
from Car import Car  # 导入自定义的Car类

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))

# 创建Car实例
car = Car(50, 50)

# 定义移动的像素数
move_pixels = 50

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 根据按键设置汽车的新目标位置
            if event.key == pygame.K_UP:
                car.set_target(car.current_x, car.current_y - move_pixels)
            elif event.key == pygame.K_DOWN:
                car.set_target(car.current_x, car.current_y + move_pixels)
            elif event.key == pygame.K_LEFT:
                car.set_target(car.current_x - move_pixels, car.current_y)
            elif event.key == pygame.K_RIGHT:
                car.set_target(car.current_x + move_pixels, car.current_y)

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
