import pygame
import math

class Car:
    def __init__(self, center_x, center_y, size, speed=5, image_path="images/car2_dilated.png"):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.speed = speed
        self.image_path = image_path
        self.target_x = center_x
        self.target_y = center_y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def set_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

    def update(self, screen):
        distance = math.hypot(self.target_x - self.center_x, self.target_y - self.center_y)
        flag = False
        if distance < self.speed:
            self.center_x = self.target_x
            self.center_y = self.target_y
            flag = True
        else:
            angle = math.atan2(self.target_y - self.center_y, self.target_x - self.center_x)
            self.center_x += self.speed * math.cos(angle)
            self.center_y += self.speed * math.sin(angle)
        
        screen.blit(self.image, (self.center_x - self.size // 2, self.center_y - self.size // 2))
        return flag


if __name__ == "__main__":
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Car Movement')
    clock = pygame.time.Clock()

    # Create Car object
    car = Car(400, 300, 100)

    running = True
    while running:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                target_x, target_y = event.pos
                car.set_target(target_x, target_y)
        
        car.update(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
