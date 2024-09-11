import pygame
import math

class Car:
    def __init__(self, x, y, speed=5, size=100):
        self.current_x = x
        self.current_y = y
        self.speed = speed
        self.size = size
        self.target_x = x
        self.target_y = y
        self.image = pygame.image.load("images/car.jpg")
        self.image = pygame.transform.scale(self.image, (size, size))
    
    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

    def draw(self, screen):
        self.render(screen)

    def update(self):
        dx = self.target_x - self.current_x
        dy = self.target_y - self.current_y
        distance = math.hypot(dx, dy)
        
        if distance < self.speed:
            self.current_x = self.target_x
            self.current_y = self.target_y
        else:
            angle = math.atan2(dy, dx)
            self.current_x += self.speed * math.cos(angle)
            self.current_y += self.speed * math.sin(angle)

    def render(self, screen):
        screen.blit(self.image, (self.current_x, self.current_y))

if __name__ == "__main__":

    # 初始化 Pygame
    pygame.init()

    # 设置屏幕大小
    screen = pygame.display.set_mode((800, 600))

    # 设置窗口标题
    pygame.display.set_caption("Car Simulation")

    # 实例化一个Car对象
    car = Car(100, 100)

    # 运行主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 更新汽车位置
        car.update()

        # 绘制屏幕
        screen.fill((255, 255, 255))
        car.render(screen)
        pygame.display.flip()

        # 设置目标位置（测试用，实际应用中可以根据具体需求设置）
        car.set_target(400, 300)

        # 控制帧率
        pygame.time.Clock().tick(30)

    pygame.quit()
