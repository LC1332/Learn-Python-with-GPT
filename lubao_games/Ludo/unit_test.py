import pygame
import random
import time
import os
from Dice import Dice
from ChessBoard import ChessBoard
from Car import Car
from play_audio import play_audio

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dice Roll Animation')
clock = pygame.time.Clock()

grid_size = 100

# Create Dice object
dice = Dice(400, 300, 100)

# Create ChessBoard object
chess_board = ChessBoard(800, 600, grid_size, 20)

x0, y0 = chess_board.get_center( 0 )

car = Car( x0, y0 , grid_size + grid_size // 4 )


running = True
dice_in_run = False
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        # 如果按下空格，则重新运行dice.roll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_result = dice.roll()
                dice_in_run = True
        if event.type == pygame.QUIT:
            running = False
    
    if not dice.update(screen):
        # Animation is still playing
        pass
    else:
        # Animation finished
        if dice_in_run:
            print(f"Dice runing done result: {dice_result}")
            dice_in_run = False
        pass

    chess_board.render(screen)
    car.update(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
