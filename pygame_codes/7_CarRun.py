import pygame
from Car import Car

# 初始化Pygame
pygame.init()

# 定义屏幕尺寸
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))

# 创建四个汽车对象，放置在屏幕的四个角
cars = [
    Car(x=0, y=0, size=50),
    Car(x=screen_size-50, y=0, size=50),
    Car(x=0, y=screen_size-50, size=50),
    Car(x=screen_size-50, y=screen_size-50, size=50),
]

# 定义背景颜色和汽车颜色
background_color = (255, 255, 255)
car_color = (0, 0, 255)

# 设置每辆车的目标为前一辆车的位置
for i in range(1, len(cars)):
    cars[i].set_target(cars[i-1].current_x, cars[i-1].current_y)

# 游戏主循环
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新每辆车的位置
    for car in cars:
        car.update()

    # 重新设定目标
    for i in range(1, len(cars)):
        cars[i].set_target(cars[i-1].current_x, cars[i-1].current_y)

    # 李鲁鲁老师手动添加
    # cars[0].set_target(cars[-1].current_x, cars[-1].current_y)

    # 清屏
    screen.fill(background_color)

    # 渲染每辆车
    for car in cars:
        car.render(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()
