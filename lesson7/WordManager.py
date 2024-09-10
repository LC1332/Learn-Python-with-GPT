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

    def get_word_data(self, K=4):
        sorted_words = sorted(self.english2score.items(), key=lambda item: item[1])
        lowest_score_words = [word for word, score in sorted_words[:K]]
        selected_word = random.choice(lowest_score_words)
        return {'english': selected_word, 'chinese_meaning': self.english2chinese[selected_word]}

    def get_M_words(self, M=4):
        sorted_words = sorted(self.english2score.items(), key=lambda item: item[1])
        lowest_score_words = [word for word, score in sorted_words[:2 * M]]
        selected_words = random.sample(lowest_score_words, M)
        return selected_words

    def add_score(self, english_word, delta=1):
        self.english2score[english_word] = min(100, self.english2score[english_word] + delta)
        self.save()

    def minus_score(self, english_word, delta=1):
        self.english2score[english_word] = max(0, self.english2score[english_word] - delta)
        self.save()

    def get_alternative(self, english_word, n=3):
        alternatives = [meaning for word, meaning in self.english2chinese.items() if word != english_word]
        return random.sample(alternatives, n)

# 测试代码
if __name__ == "__main__":
    from utils import word_datas
    print(len(word_datas))
    manager = WordManager(word_datas)
    
    # 测试 get_word_data(K=4)
    print("初始单词数据:", manager.get_word_data(K=4))
    
    manager.add_score("apple", 1)
    print("增加分数后:", manager.get_word_data(K=4))
    
    manager.minus_score("banana", 1)
    print("减少分数后:", manager.get_word_data(K=4))
    
    alternatives = manager.get_alternative("apple")
    print("苹果的替代词:", alternatives)
    
    # 测试 get_M_words(M=4)
    words = manager.get_M_words(M=4)
    print("获取M个单词:", words)
    
    # 保存数据
    manager.save()
    
    # 加载数据
    new_manager = WordManager(word_datas)
    new_manager.load()
    print("加载后的分数:", new_manager.english2score)
