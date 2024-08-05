import pygame
import sys
from Car import Car
from random import randint


#######从第五节课复制而来的函数

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

############

# 初始化 Pygame
pygame.init()

# 屏幕设置
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Simulation")

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 初始化汽车列表
cars = []

# 生成汽车位置并设置目标
def regenerate_cars(num_cars):
    global cars
    cars.clear()
    points = random_points(num_cars, min_distance=50, screen_width=screen_width, screen_height=screen_height)
    
    for i in range(num_cars):
        if i < len(points):
            x, y = points[i]
            car = Car(x=x, y=y)
            car.set_target(randint(0, screen_width), randint(0, screen_height))
            cars.append(car)
        else:
            # 将多余的汽车目标设置到屏幕外
            car = Car(x=randint(0, screen_width), y=randint(0, screen_height))
            car.set_target(screen_width + 200, screen_height + 200)
            cars.append(car)

# 主循环
def main():
    clock = pygame.time.Clock()
    regenerate_cars(1)  # 初始化时生成1辆汽车

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    num_cars = event.key - pygame.K_0
                    regenerate_cars(num_cars)

        # 更新汽车状态
        for car in cars:
            car.update()

        # 绘制
        screen.fill(WHITE)
        for car in cars:
            car.render(screen)

        pygame.display.flip()
        clock.tick(60)  # 控制帧率

if __name__ == "__main__":
    main()
