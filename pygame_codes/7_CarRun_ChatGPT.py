import pygame
from Car import Car

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((600, 600))

# 设置窗口标题
pygame.display.set_caption("Car Simulation")

# 创建4个汽车实例，并初始化它们在屏幕四个角的位置
cars = [
    Car(0, 0, size=50),
    Car(550, 0, size=50),
    Car(550, 550, size=50),
    Car(0, 550, size=50)
]

# 运行主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新汽车位置
    for i in range(len(cars)):
        if i == 0:
            cars[i].set_target(cars[-1].current_x, cars[-1].current_y)
        else:
            cars[i].set_target(cars[i-1].current_x, cars[i-1].current_y)
        cars[i].update()

    # 绘制屏幕
    screen.fill((255, 255, 255))
    for car in cars:
        car.render(screen)
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(30)

pygame.quit()
