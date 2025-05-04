import pygame
import time
import random
pygame.init()
# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# 游戏变量
snake_block = 20  # 每个蛇块的大小
snake_speed = 5  # 蛇的移动速度
snake_list = []  # 存储蛇身体的列表
snake_length = 1  # 蛇的初始长度
# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# 字体设置
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
# 绘制蛇的函数
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
# 显示分数的函数
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    screen.blit(value, [0, 0])
# 游戏主循环
def gameLoop():
    game_over = False
    game_close = False
    # 蛇的初始位置
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    snake_length = 1  # 蛇的初始长度

    # 随机生成食物的位置
    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
    while not game_over:
        while game_close == True:
            screen.fill(blue)
            font_style = pygame.font.SysFont(None, 50)
            mesg = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            screen.blit(mesg, [screen_width / 6, screen_height / 3])
            Your_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)
        Your_score(snake_length - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            snake_length += 1
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

