import tkinter as tk
from WordManager import WordManager
import random

# 初始化WordManager
# word_datas = [...]  # 填入你的word_datas
# 这里手动修改
from utils import word_datas
word_manager = WordManager(word_datas)

# 创建主窗口
root = tk.Tk()
root.title("Word Trainer")

# 定义全局变量
current_word = None

# 获取并显示单词
def display_word():
    global current_word
    current_word = word_manager.get_word_data()
    word_label.config(text="选择这个单词的中文意思: " + current_word['english'])

# 获取备选答案
def get_answers():
    alternatives = word_manager.get_alternative(current_word['english'], 3)
    alternatives.append(current_word['chinese_meaning'])
    random.shuffle(alternatives)
    return alternatives

# 更新答案选项
def update_answers():
    answers = get_answers()
    for i, answer in enumerate(answers):
        buttons[i].config(text=answer, command=lambda ans=answer: check_answer(ans))

# 检查答案
def check_answer(selected_answer):
    if selected_answer == current_word['chinese_meaning']:
        word_manager.add_score(current_word['english'])
    else:
        word_manager.minus_score(current_word['english'])
    display_word()
    update_answers()

# 创建单词标签
word_label = tk.Label(root, text="", font=("Arial", 16))
word_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 初始化单词和答案
display_word()

# 创建答案按钮
buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=20, height=2, command=lambda: None)
    button.grid(row=1, column=i, padx=10, pady=10)
    buttons.append(button)

# 更新答案按钮
update_answers()

# 运行主循环
root.mainloop()
