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

class Car:
    def __init__(self, x, y, size, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.move_amount = 1

    def update(self):
        move_direction_x = random.choice([-1, 1])
        move_direction_y = random.choice([-1, 1])
        self.rect.x += move_direction_x * self.move_amount
        self.rect.y += move_direction_y * self.move_amount

    def render(self, screen):
        screen.blit(self.image, self.rect)

# 创建Car对象
car = Car(screen_width // 2, screen_height // 2, 100, 'images/car.jpg')

# 游戏主循环
running = True
while running:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新小汽车位置
    car.update()

    # 渲染背景和汽车
    screen.fill((255, 255, 255))  # 填充背景为白色
    car.render(screen)

    # 更新显示
    pygame.display.flip()

    # 等待200毫秒
    time.sleep(0.2)

# 退出Pygame
pygame.quit()
