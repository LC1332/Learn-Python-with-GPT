import pygame
import random
import math

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("汽车游戏")

# 加载汽车图片并调整大小
car_image = pygame.image.load('images/car.jpg')
car_image = pygame.transform.scale(car_image, (100, 100))

# 随机生成点的函数，保证任意两个点之间的距离大于 min_distance
import random
import math

def random_points(N, min_distance, screen_width, screen_height):
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def is_valid(point, points, min_distance):
        return all(distance(point, p) >= min_distance for p in points)

    points = []
    max_attempts = 10

    for _ in range(N):
        best_point = None
        max_min_distance = -1

        for _ in range(max_attempts):
            new_point = (random.uniform(0, screen_width), random.uniform(0, screen_height))
            min_dist = min([distance(new_point, p) for p in points], default=float('inf'))

            if min_dist >= min_distance:
                best_point = new_point
                break

            if min_dist > max_min_distance:
                max_min_distance = min_dist
                best_point = new_point

        points.append(best_point)

    return points


# 主循环
running = True
cars = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                num_cars = event.key - pygame.K_0
                cars = random_points(num_cars, 120, screen_width, screen_height)

    # 填充背景颜色
    screen.fill((255, 255, 255))

    # 绘制汽车
    for car_position in cars:
        screen.blit(car_image, car_position)

    # 更新显示
    pygame.display.flip()

pygame.quit()
