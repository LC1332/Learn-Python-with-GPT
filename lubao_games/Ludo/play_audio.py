from VolcanoTTS import get_audio
import pygame
import time
import threading

def play_audio(text, if_block=True):
    # 获取音频文件路径
    audio_file_path = get_audio(text)
    
    # 初始化 pygame.mixer
    pygame.mixer.init()
    
    # 停止当前播放的音频（如果有）
    pygame.mixer.music.stop()

    # 加载音频文件
    pygame.mixer.music.load(audio_file_path)
    
    # 播放音频
    pygame.mixer.music.play()
    
    if if_block:
        # 阻塞模式，等待音频播放完成
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    else:
        return
        # # 非阻塞模式，在后台线程中播放音频
        # def wait_for_audio():
        #     while pygame.mixer.music.get_busy():
        #         time.sleep(0.1)
        
        # # 启动后台线程
        # threading.Thread(target=wait_for_audio, daemon=True).start()

# 示例用法
if __name__ == "__main__":
    pygame.init()
    play_audio("你答对了吗？", False )
    play_audio("你答对了吗？")
    pygame.quit()