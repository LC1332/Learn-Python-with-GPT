import os
import pygame
from pydub import AudioSegment
from pydub.generators import Sine

# 定义音符频率
notes_freq = {
    '1': 261.63,  # C4
    '2': 293.66,  # D4
    '3': 329.63,  # E4
    '4': 349.23,  # F4
    '5': 392.00,  # G4
    '6': 440.00,  # A4
    '7': 493.88,  # B4
    '8': 523.25,  # C5
    '9': 587.33,  # D5
    '0': 659.25   # E5
}

# 创建piano_sounds目录
if not os.path.exists('piano_sounds'):
    os.makedirs('piano_sounds')

# 生成音频文件
for note, freq in notes_freq.items():
    sound = Sine(freq).to_audio_segment(duration=1000)
    sound.export(f'piano_sounds/{note}.wav', format="wav")

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Piano Visualizer")
clock = pygame.time.Clock()

# 定义颜色
active_color = (0, 255, 0)  # 激活时的颜色
inactive_color = (255, 255, 255)  # 非激活时的颜色

# 加载音频文件
sounds = {}
keys_active = {}
for note in notes_freq:
    sounds[note] = pygame.mixer.Sound(f'piano_sounds/{note}.wav')
    keys_active[note] = False  # 按键活动状态

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in sounds:
                sounds[event.unicode].play(-1)
                keys_active[event.unicode] = True  # 标记为活动
        elif event.type == pygame.KEYUP:
            if event.unicode in sounds:
                sounds[event.unicode].stop()
                keys_active[event.unicode] = False  # 标记为非活动

    # 绘制每个音符的可视化
    screen.fill((0, 0, 0))  # 用黑色填充屏幕
    for i, note in enumerate(notes_freq):
        color = active_color if keys_active[note] else inactive_color
        pygame.draw.rect(screen, color, (i * 64, 0, 60, 480))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
