import pygame
import random
import time
import os
from Dice import Dice
from ChessBoard import ChessBoard
from Car import Car
from play_audio import play_audio

grid_size = 200
max_grid_num = 15
screen_width = 1600
screen_height = 1000

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Dice Roll Animation')
clock = pygame.time.Clock()


# Create Dice object
dice = Dice(screen_width//2, screen_height//2, grid_size)

# Create ChessBoard object
chess_board = ChessBoard(screen_width, screen_height, grid_size, max_grid_num)

x0, y0 = chess_board.get_center(0)
car = Car(x0, y0, grid_size + grid_size // 4)

running = True
dice_in_run = False

# Initialize status and current index
status = "waiting_dice"
current_index = 0

car_in_target = False

while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and status == "waiting_dice":
                play_audio("开始扔骰子")
                dice_result = dice.roll()
                dice_in_run = True
                status = "playing_dice"
        if event.type == pygame.QUIT:
            running = False

    dice_update =  dice.update(screen)

    if status == "playing_dice":
        if not dice_update:
            # Animation is still playing
            pass
        else:
            # Animation finished
            if dice_in_run:
                print(f"Dice runing done result: {dice_result}")
                dice_in_run = False
                status = "asking_question"
                print(dice.result)
    
    if status == "asking_question":
        play_audio("鲁宝,")
        play_audio(f"{current_index + 1}加{dice_result}等于几啊？")
        status = "moving_car"
        move_count = -1
        start_position = current_index + 1
    
    if status == "moving_car":
        

        if car_in_target:
            move_count+= 1
            if move_count < dice_result:
                print("开始移动汽车")
                target_index = current_index + 1
                # play_audio(f"{current_index+}")
                if target_index >= max_grid_num:
                    target_index = max_grid_num   
                    status = "answer_question"

                tx,ty = chess_board.get_center(target_index)
                print(tx,ty)
                car.set_target(tx, ty)
                current_index += 1

                car_in_target = car.update(screen)
                print(car_in_target)
                
            else:
                status = "answer_question"
    
    if status == "answer_question":
        result_sum = start_position + dice_result
        play_audio(f"{start_position}加{dice_result}等于{result_sum}")
        play_audio("你答对了吗？")
        
        if result_sum < max_grid_num:
            play_audio("还没有走到终点哦，再扔一次骰子吧。", if_block = False )
            status = "waiting_dice"
        else:
            if result_sum == max_grid_num:
                play_audio(f"正好是{max_grid_num}，到终点啦，让我们再玩一局吧", if_block = False )
            else:
                play_audio(f"超过{max_grid_num}了，到终点啦，让我们再玩一局吧", if_block = False )
            current_index = 0
            car.set_target(*chess_board.get_center(0))
            status = "waiting_dice"
    
    dice_update =  dice.update(screen)
    chess_board.render(screen)
    car_in_target = car.update(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
