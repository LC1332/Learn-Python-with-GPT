import pygame
import math
import wave
import struct

# 初始化Pygame
pygame.init()

# 定义音符频率
note_freqs = {
    'do': 261.63,  # C4
    're': 293.66,  # D4
    'mi': 329.63,  # E4
    'fa': 349.23,  # F4
    'so': 392.00   # G4
}

# 定义采样率
sampling_rate = 44100

# 生成一个音符的函数
def generate_note(freq, duration, filename):
    # 创建WAV文件
    obj = wave.open(filename, 'w')
    obj.setnchannels(1)  # 单声道
    obj.setsampwidth(2)  # 两个字节
    obj.setframerate(sampling_rate)

    # 生成正弦波
    for i in range(int(sampling_rate * duration)):
        value = int(32767.0 * math.sin(2 * math.pi * freq * i / sampling_rate))
        data = struct.pack('<h', value)
        obj.writeframesraw(data)

    obj.close()

# 初始化时生成WAV文件
for note, freq in note_freqs.items():
    generate_note(freq, 0.5, f'{note}.wav')

# 加载生成的WAV文件
note_sounds = {
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
            if event.key in note_sounds:
                # 播放对应的音符
                note_sounds[event.key].play(maxtime=duration)

# 退出Pygame
pygame.quit()