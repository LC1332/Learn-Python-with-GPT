import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 153, 213)

# 设置屏幕大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20  # 每个方格为20*20像素
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 创建屏幕对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 设置字体
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# 定义蛇类
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)
        self.grow = False
        self.length = 1

    def move(self):
        head_x, head_y = self.positions[0]
        new_x = head_x + self.direction[0]
        new_y = head_y + self.direction[1]

        # 如果蛇碰到边界则从另一边穿出
        new_x %= GRID_WIDTH
        new_y %= GRID_HEIGHT

        new_position = (new_x, new_y)

        # 插入新的头部位置
        self.positions.insert(0, new_position)
        if not self.grow and len(self.positions) > 30:
            self.positions.pop()
        self.grow = False

    def change_direction(self, direction):
        opposite_direction = (-self.direction[0], -self.direction[1])
        if direction != opposite_direction:
            self.direction = direction

    def grow_snake(self):
        self.grow = True
        self.length += 1

    def draw(self, screen):
        rendered_pos = set()
        for pos in self.positions:
            if pos not in rendered_pos:
                pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                rendered_pos.add(pos)
            else:
                # render into blue
                pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            # pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# 定义食物类
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def spawn(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# 显示分数的函数
def display_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# 主游戏循环
def game_loop():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    snake_speed = 10  # 控制蛇的移动速度
    game_over = False
    game_close = False

    while not game_over:
        while game_close:
            screen.fill(BLUE)
            mesg = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        # 移动蛇
        snake.move()

        # 检查是否吃到食物
        if snake.positions[0] == food.position:
            snake.grow_snake()
            food.spawn()

        # 绘制
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        display_score(snake.length - 1)
        pygame.display.update()

        # 控制帧率
        clock.tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
