import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 设置屏幕大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20  # 每个方格为20*20像素
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 创建屏幕对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 定义蛇类
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        new_x = head_x + self.direction[0]
        new_y = head_y + self.direction[1]
        new_position = (new_x, new_y)

        # 如果蛇吃到自己或碰到边界，游戏结束
        if new_position in self.positions or new_x < 0 or new_y < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
            raise Exception("Game Over")

        # 插入新的头部位置
        self.positions.insert(0, new_position)
        if not self.grow:
            self.positions.pop()
        self.grow = False

    def change_direction(self, direction):
        # 防止蛇反向移动
        opposite_direction = (-self.direction[0], -self.direction[1])
        if direction != opposite_direction:
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        for pos in self.positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# 定义食物类
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def spawn(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# 主游戏循环
def game_loop():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while True:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
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
        try:
            snake.move()
        except Exception as e:
            print(e)
            pygame.quit()
            return

        # 检查是否吃到食物
        if snake.positions[0] == food.position:
            snake.grow_snake()
            food.spawn()

        # 绘制
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()

        # 控制帧率
        clock.tick(3)

if __name__ == "__main__":
    game_loop()
