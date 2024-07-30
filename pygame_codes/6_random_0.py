import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 设置窗口大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置标题
pygame.display.set_caption('移动的小汽车')

# 加载图片并调整大小
car_image = pygame.image.load('images/car.jpg')
car_image = pygame.transform.scale(car_image, (100, 100))

# 获取图片矩形区域
car_rect = car_image.get_rect()

# 设置初始位置
car_rect.topleft = (screen_width // 2, screen_height // 2)

# 设置移动速度
move_amount = 1

# 游戏主循环
running = True
while running:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动小汽车
    move_direction_x = random.choice([-1, 1])
    move_direction_y = random.choice([-1, 1])
    car_rect.x += move_direction_x * move_amount
    car_rect.y += move_direction_y * move_amount

    # 确保小汽车不会离开窗口
    car_rect.clamp_ip(screen.get_rect())

    # 渲染背景和汽车
    screen.fill((255, 255, 255))  # 填充背景为白色
    screen.blit(car_image, car_rect)

    # 更新显示
    pygame.display.flip()

    # 等待200毫秒
    time.sleep(0.2)

# 退出Pygame
pygame.quit()