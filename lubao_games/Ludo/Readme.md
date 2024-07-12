# 飞行棋游戏

因为鲁宝已经能够背出大多数十以内的加法

https://www.bilibili.com/video/BV12r421T7pz

也已经认识了“骰子”

所以我们希望建立一个数字游戏，是一个简易版本的飞行棋。

我们先把骰子的类建立起来

```
我希望实现一个pygame的骰子类Dice，

这个类有初始化 __init__( center_x, center_y, size )

一个update的方法

和一个roll的方法

在初始化的时候，会先检查images下有没有1.jpg到6.jpg,如果没有，则会生成400*400的图片，中间渲染上较大的数字

roll()调用的时候，会记录并返回一个1到6的随机数，并且初始化类的时钟

update(screen)会根据时钟，来进行更新，前4s的时候，dice会每0.5s随机更新一张图片

在4s之后，会显示最终roll到的dice的结果。

update会返回动画仍然在播放(False) 还是已经显示最终结果(True)

请为我实现。
```

---

我们接下来要画棋盘

如果画面长宽是 800 * 600

每个正方形是100*100，那么周围一圈本身就可以容纳44个格子

```
我希望实现一个pygame的ChessBoard类

这个类会有一个初始化方法 __init__( screen_width, screen_height, grid_size, grid_num, color_type_num = 4 )

（保证grid_size能整除screen_width和screen_height）



render(screen) 会渲染这个棋盘 渲染规则如下


- 第一个正方形会渲染在grid_size//2, grid_size//2的位置
- 之后每一个正方形会依次以顺时针顺序渲染在画面的边缘
- 每个正方形的颜色会根据color_type_num的数量一次循环， default_colors 为红色 绿色 黄色 蓝色 品红 青色 粉色 白色
- 每个正方形都会根据如下代码

image = pygame.Surface((400, 400))
image.fill( color )
font = pygame.font.Font(None, 300)
text = font.render(str(number), True, (0, 0, 0))
text_rect = text.get_rect(center=(200, 200))
image.blit(text, text_rect)

生成对应的数字和图片结合的400*400的图片，再resize到grid_size

- 如果渲染的数量超过 screen_width//grid_size * 2 + screen_height//grid_size * 2 - 4，则停止渲染

```

---

我们最好生成一张粗一点的小汽车的图片

```
我希望画一张能够在pygame渲染出来的透明的png 小汽车图片

整个图片大小是400*400

小汽车用30个像素的黑色粗线条进行描绘，包含侧面的车身和轮子

保存小汽车在images/car.png

并且在pygame上以白色的背景渲染出小汽车
```

---


```
我希望实现一个Car类 这个类有初始化方法

__init__(center_x, center_y, size, speed = 5, image_path ="images/car2.png")

初始化的时候会把target_x, target_y 设置为center_x, center_y

这个类还有两个成员函数 set_target(target_x, target_y ) 和update(screen)

update的时候如果target和当前center的距离小于speed，则
直接把center设置成target

否则，则根据speed，把center向target靠近，并且渲染出小汽车
```

---

```
car2.png存储了一张png的线条画图片，但是线条太细了

可以帮我实现一个程序，让所有的线条膨胀5个像素吗？

```

---

我们来写最终完整的程序

```python
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
max_grid_num = 20

# Create Dice object
dice = Dice(400, 300, 100)

# Create ChessBoard object
chess_board = ChessBoard(800, 600, grid_size, max_grid_num)

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
    if_car_in_target = car.update(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

已知上面这段程序可以正确运行，我希望对这个程序进行修改

- 增加状态变量status， status可能是
"waiting_dice", "playing_dice", "asking_question", "moving_car","answer_question" 几个中的一个
- 增加变量 current_index, 记录car当前的位置

- 在"waiting_dice"状态下，如果用户按空格，则会调用 play_audio("开始扔骰子")，并且进入playing_dice阶段
- 在"playing_dice"状态下，如果dice.update(screen)返回True, 则进入asking_question阶段
- asking_question阶段会先后调用语音play_audio("鲁宝,") , play_audio(f"{current_index+1}加{dice_result}等于几啊？")，播放完成后，会进入moving_car阶段
- 在moving_car阶段会循环 dice_result 次
    -  每次调用car.set_target( chess_board.get_center(current_index + 1) )，并且不断检查if_car_in_target = car.update(screen)的返回值，
    - 如果if_car_in_target为True，播放play_audio(f"{current_index + 1}") 则进入下一步的循环，
    - 如果current_index+1 >= max_grid_num，则提前跳出
    - 都循环完以后进入answer_question阶段
- 在answer_question阶段，会先后调用play_audio(f"{current_index+1}加{dice_result}等于{dice_result+current_index+1}"), play_audio("你答对了吗")
    并且判断这个时候dice_result+current_index+1 和 max_grid_num的大小关系
        - dice_result+current_index+1 < max_grid_num, 调用play_audio("还没有走到终点哦，再扔一次骰子吧。")
        - dice_result+current_index+1 = max_grid_num, 调用play_audio(f"正好是{max_grid_num}，到终点啦，让我们再完一局吧")
        - dice_result+current_index+1 > max_grid_num, 调用play_audio(f"超过{max_grid_num}了，到终点啦，让我们再完一局吧")
    如果到达终点，重新初始化current_index，进入下一局游戏


