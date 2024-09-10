import tkinter as tk
from WordManager import WordManager
import random
from words2prompt import words2prompt
from question2response import question2response

# 初始化WordManager
from utils import word_datas
word_manager = WordManager(word_datas)

# 创建主窗口
root = tk.Tk()
root.title("Word Trainer")

# 定义全局变量
current_word = None
current_score_label = None  # 初始化current_score_label为全局变量

# 获取并显示单词
def display_word():
    global current_word
    global current_score_label
    current_word = word_manager.get_word_data()
    word_label.config(text="选择这个单词的中文意思: " + current_word['english'])
    if current_score_label:
        current_score_label.destroy()
    current_score_label = None

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
    global current_score_label
    if selected_answer == current_word['chinese_meaning']:
        word_manager.add_score(current_word['english'])
        current_score_label = tk.Label(root, text="正确!", fg="green", font=("Arial", 16))
    else:
        word_manager.minus_score(current_word['english'])
        current_score_label = tk.Label(root, text="错误!", fg="red", font=("Arial", 16))
    current_score_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

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

# 创建“下一个”按钮
next_button = tk.Button(root, text="下一个", command=lambda: [display_word(), update_answers()])
next_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# 创建文本框用于显示造句，并添加滚动条
sentence_text = tk.Text(root, height=15, width=50)
sentence_text.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# 创建滚动条
scrollbar = tk.Scrollbar(root, command=sentence_text.yview)
scrollbar.grid(row=4, column=4, sticky='nsew')
sentence_text['yscrollcommand'] = scrollbar.set

# 创建“陌生词造句”按钮
def generate_sentence():
    words = word_manager.get_M_words()
    prompt = words2prompt(words)
    response = question2response(prompt)
    sentence_text.delete(1.0, tk.END)  # 清空文本框
    sentence_text.insert(tk.END, response)  # 插入新的句子

sentence_button = tk.Button(root, text="陌生词造句", command=generate_sentence)
sentence_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# 运行主循环
root.mainloop()
