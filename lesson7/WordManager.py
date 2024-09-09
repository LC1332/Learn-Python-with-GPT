import json
import os
import random

class WordManager:
    def __init__(self, word_datas):
        self.english2score = {}
        self.english2chinese = {}
        for word_data in word_datas:
            self.english2score[word_data['english']] = 20
            self.english2chinese[word_data['english']] = word_data['chinese_meaning']
        self.save_path = 'data/word2score.jsonl'
        self.load()

    def save(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        with open(self.save_path, 'w') as f:
            for english, score in self.english2score.items():
                f.write(json.dumps({english: score}) + '\n')

    def load(self, file_name=None):
        file_name = file_name or self.save_path
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                for line in f:
                    data = json.loads(line)
                    self.english2score.update(data)

    def get_word_data(self):
        min_score = min(self.english2score.values())
        lowest_score_words = [word for word, score in self.english2score.items() if score == min_score]
        selected_word = random.choice(lowest_score_words)
        return {'english': selected_word, 'chinese_meaning': self.english2chinese[selected_word]}

    def add_score(self, english_word, delta=1):
        self.english2score[english_word] = min(100, self.english2score[english_word] + delta)

    def minus_score(self, english_word, delta=1):
        self.english2score[english_word] = max(0, self.english2score[english_word] - delta)

    def get_alternative(self, english_word, n=3):
        alternatives = [meaning for word, meaning in self.english2chinese.items() if word != english_word]
        return random.sample(alternatives, n)

# 测试代码
if __name__ == "__main__":
    word_datas = word_datas = [
    {"english": "apple", "chinese_meaning": "苹果"},
    {"english": "banana", "chinese_meaning": "香蕉"},
    {"english": "cat", "chinese_meaning": "猫"},
    {"english": "dog", "chinese_meaning": "狗"},
    {"english": "elephant", "chinese_meaning": "大象"},
    {"english": "fish", "chinese_meaning": "鱼"},
    {"english": "grape", "chinese_meaning": "葡萄"},
    {"english": "house", "chinese_meaning": "房子"},
    {"english": "ice", "chinese_meaning": "冰"},
    {"english": "jacket", "chinese_meaning": "夹克"},
    {"english": "kite", "chinese_meaning": "风筝"},
    {"english": "lemon", "chinese_meaning": "柠檬"},
    {"english": "monkey", "chinese_meaning": "猴子"},
    {"english": "nose", "chinese_meaning": "鼻子"},
    {"english": "orange", "chinese_meaning": "橙子"},
    {"english": "pencil", "chinese_meaning": "铅笔"},
    {"english": "queen", "chinese_meaning": "女王"},
    {"english": "rabbit", "chinese_meaning": "兔子"},
    {"english": "snake", "chinese_meaning": "蛇"},
    {"english": "tree", "chinese_meaning": "树"},
    {"english": "umbrella", "chinese_meaning": "伞"},
    {"english": "violin", "chinese_meaning": "小提琴"},
    {"english": "water", "chinese_meaning": "水"},
    {"english": "xylophone", "chinese_meaning": "木琴"},
    {"english": "yogurt", "chinese_meaning": "酸奶"},
    {"english": "zebra", "chinese_meaning": "斑马"},
    {"english": "book", "chinese_meaning": "书"},
    {"english": "cup", "chinese_meaning": "杯子"},
    {"english": "door", "chinese_meaning": "门"},
    {"english": "flower", "chinese_meaning": "花"}
]
    print(len(word_datas))
    manager = WordManager(word_datas)
    print("初始单词数据:", manager.get_word_data())
    
    manager.add_score("apple", 5)
    print("增加分数后:", manager.get_word_data())
    
    manager.minus_score("banana", 3)
    print("减少分数后:", manager.get_word_data())
    
    alternatives = manager.get_alternative("apple")
    print("苹果的替代词:", alternatives)
    
    # 保存数据
    manager.save()
    
    # 加载数据
    new_manager = WordManager(word_datas)
    new_manager.load()
    print("加载后的分数:", new_manager.english2score)
