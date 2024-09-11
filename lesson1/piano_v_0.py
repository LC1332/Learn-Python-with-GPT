import pygame
import sys

# 初始化Pygame
pygame.init()

# 加载音符声音文件
# 确保你有以下文件：do.wav, re.wav, mi.wav, fa.wav, so.wav
# 这些文件应该放在你的项目目录中
sounds = {
    pygame.K_1: pygame.mixer.Sound('do.wav'),
    pygame.K_2: pygame.mixer.Sound('re.wav'),
    pygame.K_3: pygame.mixer.Sound('mi.wav'),
    pygame.K_4: pygame.mixer.Sound('fa.wav'),
    pygame.K_5: pygame.mixer.Sound('so.wav')
}

# 设置音符持续时间
duration = 500  # 毫秒

# 创建一个窗口，大小为200x200
screen = pygame.display.set_mode((200, 200))

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 检查按键是否是我们关心的音符键
            if event.key in sounds:
                # 播放对应的音符
                sounds[event.key].play(maxtime=duration)

# 退出Pygame
pygame.quit()
sys.exit()
