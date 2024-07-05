import numpy as np
from scipy.io.wavfile import write
import os
import pygame

# 声音频率（Hz）
frequencies = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
    'D5': 587.33,
    'E5': 659.25
}

# 生成声音文件函数
def generate_sound(frequency, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# 创建声音文件目录
os.makedirs("piano_sounds", exist_ok=True)

# 生成和保存声音文件
for note, freq in frequencies.items():
    sound_wave = generate_sound(freq)
    write(f"piano_sounds/{note}.wav", 44100, sound_wave.astype(np.float32))

# 初始化pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Piano")

# 加载声音文件
sounds = {
    pygame.K_1: pygame.mixer.Sound("piano_sounds/C4.wav"),
    pygame.K_2: pygame.mixer.Sound("piano_sounds/D4.wav"),
    pygame.K_3: pygame.mixer.Sound("piano_sounds/E4.wav"),
    pygame.K_4: pygame.mixer.Sound("piano_sounds/F4.wav"),
    pygame.K_5: pygame.mixer.Sound("piano_sounds/G4.wav"),
    pygame.K_6: pygame.mixer.Sound("piano_sounds/A4.wav"),
    pygame.K_7: pygame.mixer.Sound("piano_sounds/B4.wav"),
    pygame.K_8: pygame.mixer.Sound("piano_sounds/C5.wav"),
    pygame.K_9: pygame.mixer.Sound("piano_sounds/D5.wav"),
    pygame.K_0: pygame.mixer.Sound("piano_sounds/E5.wav")
}

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in sounds:
                sounds[event.key].play(-1)  # -1参数使声音循环播放
        elif event.type == pygame.KEYUP:
            if event.key in sounds:
                sounds[event.key].stop()  # 停止声音播放

# 退出pygame
pygame.quit()
