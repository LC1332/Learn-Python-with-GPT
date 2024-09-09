word_datas = [
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
import gradio as gr
from WordManager import WordManager
import random

# 假设word_datas已经定义好了
word_manager = WordManager(word_datas)

def select_chinese_meaning():
    # 获取熟练度最低的单词
    word_data = word_manager.get_word_data()
    english_word = word_data['english']
    chinese_meaning = word_data['chinese_meaning']

    # 获取三个备选的中文意思
    alternatives = word_manager.get_alternative(english_word, n=3)

    # 将正确的中文意思加入备选列表并打乱顺序
    alternatives.append(chinese_meaning)
    random.shuffle(alternatives)

    # 创建下拉菜单选项格式
    options = [(meaning, meaning) for meaning in alternatives]

    # 返回单词和打乱后的选项
    return english_word, chinese_meaning, options

def check_answer(english_word, user_choice, chinese_meaning):
    # 检查用户选择是否正确
    if user_choice == chinese_meaning:
        word_manager.add_score(english_word)
        return "正确！点击'下一题'继续。", None
    else:
        word_manager.minus_score(english_word)
        return "错误，正确答案是：{}。点击'下一题'继续。".format(chinese_meaning), chinese_meaning

def update_interface():
    english_word, chinese_meaning, options = select_chinese_meaning()
    english_word_textbox.value = english_word
    options_dropdown.choices = options
    correct_meaning_textbox.value = chinese_meaning
    result_textbox.value = ""
    return english_word, chinese_meaning, options

def gradio_interface():
    # 创建Gradio界面
    with gr.Blocks() as demo:
        gr.Markdown("选择这个单词的中文意思")

        # 输出单词
        english_word_textbox = gr.Textbox(label="英文单词", interactive=False)

        # 输出选项
        options_dropdown = gr.Dropdown(label="选项", choices=[])

        # 隐藏的文本框用于存储正确答案
        correct_meaning_textbox = gr.Textbox(visible=False)

        # 提交按钮
        submit_button = gr.Button("提交")

        # 下一题按钮
        next_button = gr.Button("下一题")

        # 输出结果
        result_textbox = gr.Textbox(label="结果", interactive=False)

        # 当提交按钮被点击时
        submit_button.click(
            fn=check_answer,
            inputs=[english_word_textbox, options_dropdown, correct_meaning_textbox],
            outputs=[result_textbox, correct_meaning_textbox]
        )

        # 当下一题按钮被点击时
        next_button.click(
            fn=update_interface,
            outputs=[english_word_textbox, correct_meaning_textbox, options_dropdown.choices]
        )

        # 初始化界面
        update_interface()

    return demo

# 运行Gradio界面
demo = gradio_interface()
demo.launch()
