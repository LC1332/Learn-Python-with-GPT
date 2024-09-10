
# "I am learning English, and I am not very familiar with the following words:\n\n"
#         f"{words_str}\n\n"
#         "Please help me create a short story that includes these words, and then translate the story back into Chinese."


def words2prompt(words):
    # 将单词列表转换为字符串，每个单词用单引号包围，并用逗号和空格分隔
    words_str = ", ".join(["{}".format(word) for word in words])
    
    # 构建prompt字符串
    prompt = (
        "I am learning English, and I am not very familiar with the following words:\n\n"
        f"{words_str}\n\n"
        "Please help me create a short story that includes these words, and then translate the story back into Chinese."
    )
    
    return prompt

if __name__ == "__main__":
    from utils import word_datas
    from WordManager import WordManager

    word_manager = WordManager(word_datas)
    words = word_manager.get_M_words()

#     Enervate - 使衰弱，使无力
# Precipitous - 险峻的，匆忙的
# Loquacious - 健谈的，话多的
# Ineffable - 无法表达的，难以言喻的
# Soporific - 催眠的，令人昏昏欲睡的 6.hubristic - 傲慢的，狂妄自大的
# Perfunctory - 敷衍的，马虎的
# Ostentatious - 炫耀的，卖弄的
# Intransigent - 倔强的，不妥协的
# Mellifluous - 甜美的，悦耳的（通常指声音或音乐）

    # change words into a GRE difficulty words
    words = ["ineffable","mellifluous","Perfunctory","ostentatious"]
    
    prompt = words2prompt(words)
    print(prompt)

    from question2response import question2response
    response = question2response(prompt)
    print("---\n",response)

