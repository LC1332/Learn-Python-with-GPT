import base64
import json
import uuid
import requests
import os
from dotenv import load_dotenv

default_save_folder = "audios/"
default_memory_file = "text_audiobooks.jsonl"
text_audio_table = None

proxies = {
    'http': 'http://127.0.0.1:8234',
    'https': 'http://127.0.0.1:8234',
}

class VolcanoTTS:
    def __init__(self, voice_type = None, speed = None):
        load_dotenv()

        # 填写平台申请的appid, access_token以及cluster
        self.appid = os.getenv('VOLCANO_APP_ID')
        self.access_token = os.getenv('VOLCANO_ACCESS_TOKEN')

        self.cluster = "volcano_tts"
        if voice_type is None:
            self.voice_type = "BV426_streaming"
        else:
            self.voice_type = voice_type
        if speed is None:
            self.speed = 0.9
        else:
            self.speed = speed
        self.host = "openspeech.bytedance.com"
        self.api_url = f"https://{self.host}/api/v1/tts"
        self.header = {"Authorization": f"Bearer;{self.access_token}"}

    def text2audio(self, content, save_name):
        request_json = {
            "app": {
                "appid": self.appid,
                "token": "access_token",
                "cluster": self.cluster
            },
            "user": {
                "uid": "388808087185088"
            },
            "audio": {
                "voice_type": self.voice_type,
                "encoding": "mp3",
                "speed_ratio": self.speed,
                "volume_ratio": 1.0,
                "pitch_ratio": 1.0,
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": content,
                "text_type": "plain",
                "operation": "query",
                "with_frontend": 1,
                "frontend_type": "unitTson"
            }
        }

        try:
            # resp = requests.post(self.api_url, json.dumps(request_json), headers=self.header, timeout = 40)
            if proxies is not None:
                resp = requests.post(self.api_url, json.dumps(request_json), headers=self.header, proxies=proxies, timeout = 40)
            # print(f"resp body: \n{resp.json()}")
            if "data" in resp.json():
                data = resp.json()["data"]
                with open(save_name, "wb") as file_to_save:
                    file_to_save.write(base64.b64decode(data))
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

# 初始化和加载现有音频数据
def load_audio_memory():
    global text_audio_table
    memory_file_path = os.path.join(default_save_folder, default_memory_file)
    if os.path.exists(memory_file_path):
        text_audio_table = {}
        with open(memory_file_path, "r", encoding="utf-8") as file:
            for line in file:
                entry = json.loads(line)
                text_audio_table[entry["text"]] = entry["audio_file_name"]
    else:
        text_audio_table = {}

_tts = None

def get_audio(text):
    global text_audio_table

    # 确保音频数据已加载
    if not text_audio_table:
        load_audio_memory()

    # 检查是否已存在音频
    if text in text_audio_table:
        return os.path.join(default_save_folder, text_audio_table[text])
    
    global _tts
    if not _tts:
        _tts = VolcanoTTS(voice_type="BV426_streaming")
    # 如果不存在，则生成新的音频
    tts = _tts
    audio_file_name = f"{uuid.uuid4()}.mp3"
    audio_file_path = os.path.join(default_save_folder, audio_file_name)

    tts.text2audio(text, audio_file_path)

    # 更新内存和文件
    text_audio_table[text] = audio_file_name
    memory_file_path = os.path.join(default_save_folder, default_memory_file)
    with open(memory_file_path, "a", encoding="utf-8") as file:
        json.dump({"text": text, "audio_file_name": audio_file_name}, file, ensure_ascii=False)
        file.write("\n")  # 添加新行

    return audio_file_path



if __name__ == "__main__":
    text = "还没有走到终点哦，再扔一次骰子吧。"
    get_audio(text)