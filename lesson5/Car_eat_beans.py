import pygame
from Car import Car
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))

# 创建Car实例
car = Car(50, 50)

# 定义移动的像素数
move_pixels = 50

# 豆子的大小和数量
bean_size = 30
bean_count = 3
beans = []

# 分数
score = 0
font = pygame.font.Font(None, 36)

# 生成豆子
def generate_beans():
    global beans
    beans = []
    for _ in range(bean_count):
        bean_x = random.randint(0, 800 - bean_size)
        bean_y = random.randint(0, 600 - bean_size)
        beans.append(pygame.Rect(bean_x, bean_y, bean_size, bean_size))

# 生成初始豆子
generate_beans()

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car.set_target(car.current_x, max(car.current_y - move_pixels, 0))
            elif event.key == pygame.K_DOWN:
                car.set_target(car.current_x, min(car.current_y + move_pixels, 600 - car.size))
            elif event.key == pygame.K_LEFT:
                car.set_target(max(car.current_x - move_pixels, 0), car.current_y)
            elif event.key == pygame.K_RIGHT:
                car.set_target(min(car.current_x + move_pixels, 800 - car.size), car.current_y)

    # 更新汽车位置
    car.update()

    # 检测汽车是否撞到豆子
    car_rect = pygame.Rect(car.current_x - car.size // 2, car.current_y - car.size // 2, car.size, car.size)
    for bean in beans[:]:  # 使用副本进行遍历，以便在迭代时修改列表
        if car_rect.colliderect(bean):
            beans.remove(bean)
            score += 1
            if len(beans) == 0:
                generate_beans()

    # 填充背景色
    screen.fill((255, 255, 255))

    # 绘制豆子
    for bean in beans:
        pygame.draw.rect(screen, (0, 255, 0), bean)

    # 绘制汽车
    car.draw(screen)

    # 显示分数
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 更新屏幕显示
    pygame.display.flip()

    # 控制游戏帧率
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
