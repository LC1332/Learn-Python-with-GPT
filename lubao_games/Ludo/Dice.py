import pygame
import random
import time
import os

class Dice:
    def __init__(self, center_x, center_y, size):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.dice_images = []
        self.load_images()
        self.result = 3
        
        self.ANIMATE_DURATION = 2
        self.start_time = time.time() - self.ANIMATE_DURATION
        self.animating = False
        self.current_image = None

    def load_images(self):
        for i in range(1, 7):
            image_path = f'images/{i}.jpg'
            if not os.path.exists(image_path):
                self.create_image(i, image_path)
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (self.size, self.size))
            self.dice_images.append(image)
            
    def create_image(self, number, path):
        image = pygame.Surface((400, 400))
        image.fill((255, 255, 255))
        font = pygame.font.Font(None, 300)
        text = font.render(str(number), True, (0, 0, 0))
        text_rect = text.get_rect(center=(200, 200))
        image.blit(text, text_rect)
        pygame.image.save(image, path)

    def roll(self):
        self.result = random.randint(1, 6)
        self.start_time = time.time()
        self.animating = True
        return self.result

    def update(self, screen):
        
        elapsed_time = time.time() - self.start_time
        small_time = 0.3
        if elapsed_time < self.ANIMATE_DURATION - small_time:
            # if int(elapsed_time * 2) % 2 == 0:
            self.current_image = random.choice(self.dice_images)
        elif elapsed_time < self.ANIMATE_DURATION:
            self.current_image = self.dice_images[self.result - 1]
        else:
            self.current_image = self.dice_images[self.result - 1]
            self.animating = False
        
        screen.blit(self.current_image, (self.center_x - self.size // 2, self.center_y - self.size // 2))
        return not self.animating


if __name__ == '__main__':
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Dice Roll Animation')
    clock = pygame.time.Clock()

    # Create Dice object
    dice = Dice(400, 300, 100)

    running = True
    while running:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            # 如果按下空格，则重新运行dice.roll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    num = dice.roll()
                    print(f"Dice result: {num}")
            if event.type == pygame.QUIT:
                running = False
        
        if not dice.update(screen):
            # Animation is still playing
            pass
        else:
            # Animation finished
            # print(f"Dice Rolling Done")
            pass
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
