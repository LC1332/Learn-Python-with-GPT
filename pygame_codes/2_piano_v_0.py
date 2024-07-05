import numpy as np
from scipy.io.wavfile import write
import pygame
import time

# 声音频率（Hz）
frequencies = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00
}

# 生成声音文件
def generate_sound(frequency, duration=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

sound_folder = "piano_sounds/"
import os
os.mkdir(sound_folder)

# 保存wav文件
for note, freq in frequencies.items():
    sound_wave = generate_sound(freq)
    fname = sound_folder + note + ".wav"
    write(fname, 44100, sound_wave.astype(np.float32))

# 初始化pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Sound Example")

# 加载声音文件
sounds = {
    pygame.K_1: pygame.mixer.Sound(sound_folder + "C.wav"),
    pygame.K_2: pygame.mixer.Sound(sound_folder + "D.wav"),
    pygame.K_3: pygame.mixer.Sound(sound_folder + "E.wav"),
    pygame.K_4: pygame.mixer.Sound(sound_folder + "F.wav"),
    pygame.K_5: pygame.mixer.Sound(sound_folder + "G.wav")
}

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in sounds:
                sounds[event.key].play()
                time.sleep(0.5)  # 播放0.5秒
                sounds[event.key].stop()  # 停止播放

# 退出pygame
pygame.quit()
