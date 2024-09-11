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
    sound = Sine(freq).to_audio_segment(duration=1000)  # 生成1秒的音频
    sound.export(f'piano_sounds/{note}.wav', format="wav")  # 保存为wav文件

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()

# 加载音频文件
sounds = {}
for note in notes_freq:
    sounds[note] = pygame.mixer.Sound(f'piano_sounds/{note}.wav')

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in sounds:
                sounds[event.unicode].play(-1)  # 循环播放
        elif event.type == pygame.KEYUP:
            if event.unicode in sounds:
                sounds[event.unicode].stop()  # 停止播放

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
